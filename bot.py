import discord
from datetime import datetime
import pytz
import wikipedia
import sys
import requests
import random
from time import sleep
import tocsecret
import search_by_google as sg

print("Server Runing....")

token = tocsecret.d

client = discord.Client()

# @client.event
# async def on_member_join(member):
#     global mem
#     mem = member
# #     for channel in member.server.channels:
# #         if str(channel) == "general":
# #             await client.send_message(f"Welcome to the server {member.mention}")
#     return member



@client.event
async def on_message(message):
    id = client.get_guild(692093634333507736)
    channels = ["test-channel", "general"]
    # valid_users = ['ebulo']
    IST = pytz.timezone('Asia/Kolkata')
    hr = datetime.now(IST).hour


    if str(message.channel) in channels:
        
        excite_list = ["Wohoo", "woho", "awesome", "wow", "Yeah", "wonderfull", "insane"]
        excite_reply = ["yeahh", "Really awesome", "great", "yiepiee", "wohooooo..", "me excited", "GOOD, I like it", "glad you like it"]
        goodnight = ["Gn", "gud98", "gudn8", "gdn8", "goodnight"]

        msg = message.content
        if message.content.find("_hello") != -1:
            await message.channel.send(f"Hi {str(message.author)[0:-5]}")
            # This app is actually running on US servers.
            await message.channel.send(hr)
            if hr >= 4 and hr <=11:
                await message.channel.send("Good Morning! Have Nice day 😃")
            elif hr >= 12 and hr <= 16:
                await message.channel.send("Good Afetrnoon! 😉")
            elif hr >=17 and hr <= 23:
                await message.channel.send("Good Evening! 😎")
            elif hr >= 0 and hr <= 3:
                await message.channel.send("It's Time To Sleep 😴")
            else:
                await message.channel.send("Something Went Wrong 🛸")
            # if hour > 18 and hour <= 23:
            #     await message.channel.send("Good Evening..😯")
            # elif hour >= 00 and hour < 4:
            #     await message.channel.send("""Should I say Good Morning..Go to sleep bro....😏And wake Up early""")
            # elif hour >= 4 and hour < 12:
            #     await message.channel.send("Good Morning.. Have Nice day😃")
            # elif hour >= 12 and hour < 18:
            #     await message.channel.send("Good Evening..")


        elif message.content == "_users":
            await message.channel.send(f""" # No.of Users: {id.member_count}😮""")
        elif "_say:" in msg:
            await message.channel.send(f"{msg[5:-1]}")
        elif "thanks" in str(msg).lower():
            await message.channel.send(f"You Are Most Welcome {str(message.author)[0:-5]}🙂")
        elif "i-love-you" in str(msg).lower():
            await message.channel.send(f"I Love You too {str(message.author)[0:-5]}🥰")
        elif "-finally" in str(msg).lower():
            await message.channel.send(f"No worries {str(message.author)[0:-5]} you are finally Done, you can go to sleep now..")
        elif "_good" in str(msg[0:6]):
            await message.channel.send("Thank You..")
        elif "_welcome" in str(msg[0:10]):
            await message.channel.send("It's my Pleasure..")
        elif "_bye" in str(msg):
            await message.channel.send("Byee..")


        elif "_wiki" in str(msg).lower():
            try:
                search_result = wikipedia.summary(str(msg).replace("_wiki", ""), sentences=4)
                await message.channel.send(search_result)
            except Exception:
                await message.channel.send("Didn't Find any relevant wiki pages..")

        elif "_news" in str(msg).lower():
            news_list1 = sg.getNews("TechTopic")
            await message.channel.send(news_list1)

        elif "claide" in str(msg).lower():
            query = str(msg).replace("claide", "")
            query = str(msg).replace("Claide", "")
            result_list = sg.search_data(query)
            await message.channel.send(result_list)

            # api_key = "96a24fcb4d304307938060377016e9fc"

            # url = f"http://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey={api_key}"

            # req = requests.get(url)

            # json_format = req.json()['articles']
            # # print(json_format)
            # a = 0
            # for i in json_format:
            #     await message.channel.send("....")
            #     await message.channel.send(f"{i['title']}..{i['url']}")
            #     await message.channel.send(f"{i['urlToImage']}")
            #     sleep(4)
            #     if a == 0:
            #         await message.channel.send("That was some trending articles for today..")
            #         break
            #     a += 1

        elif "_play" in str(msg).lower():
            await message.channel.send("Play is in a Beta Mode and still working on it.")

        elif "_test" in str(msg).lower():
            abc = sg.test()
            await message.channel.send(abc)

        elif "_image-try" in str(msg).lower():
            file = discord.File("india-view.png", filename="india-view.png")
            await message.channel.send("india-view.png", file=file)

        # elif "woho" in str(msg).lower():
        #     await message.channel.send("Yeahh..")

        elif str(msg).lower() in excite_list:
            r_num = random.randint(0, len(excite_reply)-1)
            await message.channel.send(excite_reply[r_num])

        elif str(msg).lower() in goodnight:
            r_num1 = random.randint(0, len(goodnight)-1)
            await message.channel.send(f"{goodnight[r_num1]} + {str(message.author)[0:-5]}")
            sys.exit()

        elif "go-offline" in str(msg).lower():
            sys.exit()

client.run(token)