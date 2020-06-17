import discord
import datetime
import wikipedia
import sys
import requests
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
    hour = datetime.datetime.now().time().hour

    a = 0

    if str(message.channel) in channels:
        # print(message)
        excite_list = ["Wohoo", "woho", "Awesome", "wow", "Yeah"]
        msg = message.content
        if message.content.find("_hello") != -1:
            await message.channel.send(f"Hi {str(message.author)[0:-5]}")
            if hour > 18 and hour <= 23:
                await message.channel.send("Good Evening..😯")
            elif hour >= 00 and hour < 4:
                await message.channel.send("""Should I say Good Morning..Go to sleep bro....😏And wake Up early""")
            elif hour >= 4 and hour < 12:
                await message.channel.send("Good Morning.. Have Nice day😃")
            elif hour >= 12 and hour < 18:
                await message.channel.send("Good Evening..😉")
            else:
                await message.channel.send("Love You I am dead..😴")


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
        elif "_bye" in str(msg):
            await message.channel.send("Byee..")


        elif "_wiki" in str(msg).lower():
            try:
                search_result = wikipedia.summary(str(msg).replace("_wiki", ""), sentences=4)
                await message.channel.send(search_result)
            except Exception:
                await message.channel.send("Didn't Find any relevant wiki pages..")

        elif "claide" in str(msg).lower():
            query = str(msg).replace("claide", "")
            result_list = sg.search_data(query)
            await message.channel.send(result_list)

        elif "news" in str(msg).lower():
            api_key = "96a24fcb4d304307938060377016e9fc"

            url = f"http://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey={api_key}"

            req = requests.get(url)

            json_format = req.json()['articles']
            # print(json_format)
            a = 0
            for i in json_format:
                await message.channel.send("....")
                await message.channel.send(f"{i['title']}..{i['url']}")
                await message.channel.send(f"{i['urlToImage']}")
                sleep(4)
                if a == 4:
                    await message.channel.send("That was some trending articles for today..")
                    break
                a += 1


        elif "_image-try" in str(msg).lower():
            file = discord.File("india-view.png", filename="india-view.png")
            await message.channel.send("india-view.png", file=file)

        elif "woho" in str(msg).lower():
            await message.channel.send("Yeahh..")

        elif "goodnight" in str(msg).lower():
            await message.channel.send(f"Bye Good night, sleep tight😴😴")
            sys.exit()
        elif "go-offline" in str(msg).lower():
            sys.exit()

client.run(token)

# or "when" or "where" or "why" 
#  or "when" in str(msg).lower() or "where" in str(msg).lower()
