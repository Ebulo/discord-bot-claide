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
    min = datetime.now(IST).minute
    
    # bad words check.
    bad_words = ["harami", "maghyaa", "gandi","gaandi", "bando", "chodipua",  "chodi", "bala", "maghia", "jhant", "chut", "kutta", "napoonsak", "chutiya", "bharwa", "randwa", "gandwa", "bhenchod", "bhosdike", "madarchod", "laude", "lode", "bsdk", "bkl", "gand", "randi"]

    for word in bad_words:
        if message.content.count(word) > 0:
            await message.channel.purge(limit=1)
            await message.channel.send("calm bro calm, No Bad Words Please! ")

    
    # Embed Messages trial 2
    # Help for all the commands.
    if message.content == "_help":
        embed = discord.Embed(title="Help on Bot", description="Some useful commands", color=0xffff00)
        embed.add_field(name="_hello", value="Greets the user")
        embed.add_field(name="_users", value="Prints number of users")
        embed.add_field(name="_claide", value="will give url data from google search.")
        embed.add_field(name="_wiki", value="wikipedia search data")
        embed.add_field(name="_say", value="repeats what you say")
        embed.add_field(name="_news", value="shows the top 4 recent news.")
        embed.add_field(name="_thanks", value="..")
        embed.add_field(name="_good", value="..")
        embed.add_field(name="_welcome", value="..")
        embed.add_field(name="_bye", value="..")
        await message.channel.send(content=None, embed=embed)


    if str(message.channel) in channels:
        
        excite_list = ["Wohoo", "woho", "awesome", "wow", "Yeah", "wonderfull", "insane"]
        excite_reply = ["yeahh", "Really awesome", "great", "yiepiee", "wohooooo..", "me excited", "GOOD, I like it", "glad you like it"]
        goodnight = ["Gn", "gud98", "gudn8", "gdn8", "goodnight"]

        msg = message.content
        if message.content.find("_hello") != -1:
            await message.channel.send(f"Hi {str(message.author)[0:-5]}")
            await message.channel.send(str(hr) + " : " + str(min))

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

        # elif "_news" in str(msg).lower():
        #     news_list1 = sg.getNews("TechTopic")
        #     await message.channel.send(news_list1)


        elif "_news" in str(msg).lower():
            n = sg.getNews()
            color_codes = [0x27ae60, 0xf1c40f, 0xf39c12, 0xd35400, 0x0000ff, 0x204080, 0xabcdef, 0x9b59b6, 0x3498db, 0x1abc9c]

            for i in n:
                embed1 = discord.Embed(title=i['title'], description=i['desc'], color=0xff0000)
                embed1.add_field(name="Link to Page", value=f"[click here]({i['url']})")
                embed1.set_image(url=i['image'])
                await message.channel.send(content=None, embed=embed1)

        elif "_ntest" in str(msg).lower():
            n = sg.getNews()
            color_codes = [0x884f20, 0xff0000, 0x049009, 0x00ff00, 0x0000ff, 0x204080, 0xabcdef, 0x9b59b6, 0x3498db, 0x1abc9c]

            for i in n:
                embed2 = discord.Embed(title=i['title'], description=i['desc'], color=random.choice(color_codes))
                embed2.add_field(name="Link to Page", value=f"[click here]({i['url']})")
                embed2.set_image(url=i['image'])
                await message.channel.send(content=None, embed=embed2)


        elif "_claide" in str(msg).lower(): # Have changed here claide to _claide
            query = str(msg).replace("_claide", "")
            result_list = sg.search_data(query)
            await message.channel.send(result_list)

        elif "_cltest" in str(msg).lower():
            search_data = str(msg).replace("_cltest", "")
            data = sg.search_data_test(search_data)
            
            for i in data:
                embed4 = discord.Embed(title=i['title'], description=i['desc'])
                embed4.add_field(name="Check Below", value=f"[Read More]({i['url']})")
                await message.channel.send(content=None, embed=embed4)


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

        elif "_sendtest" in str(msg).lower():  #Error in sending the embed messages.
            embed3 = discord.Embed(title="Hello", description='I am a game bot', color=0x00ff00)
            embed3.add_field(name="Claide", value="bot")
            embed3.add_field(name="EbuloBot", value="PreviousBot")
            await message.channel.send(content=None, embed=embed3)


        elif "_play" in str(msg).lower():
            await message.channel.send("Play is in a Beta Mode and still working on it.")

        elif "_image-try" in str(msg).lower():
            file = discord.File("india-view.png", filename="india-view.png")
            await message.channel.send("india-view.png", file=file)

        # elif "woho" in str(msg).lower():
        #     await message.channel.send("Yeahh..")

        elif str(msg).lower() in excite_list:
            r_num = random.randint(0, len(excite_reply)-1)
            await message.channel.send(excite_reply[r_num])

        elif str(msg).lower() in bad_words:
            await message.channel.purge(limit=1)
            await message.channel.send("calm boi, No bad words please!")

        elif str(msg).lower() in goodnight:
            r_num1 = random.randint(0, len(goodnight)-1)
            await message.channel.send(f"{goodnight[r_num1]} + {str(message.author)[0:-5]}")
            sys.exit()

        elif "go-offline" in str(msg).lower():
            sys.exit()

client.run(token)