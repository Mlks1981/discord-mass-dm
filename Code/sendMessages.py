#Mlks1981
import discord
from discord.ext import commands
import json

bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready():
    print(' [!] Started Dmming Ids\n')

    with open("ids.json", "r") as file:
        data = json.load(file)

    indx = 0
    for i in data:
        indx += 1
        member = await bot.fetch_user(i)
        try:
            await member.send("INSERT INVITE")
            print(f" [+] Sent message {indx} / {len(data)}")
        except Exception as e:
            print(f" [!] {e}")

    print(" [+] Done")


#If the token belongs to a user set false if bot set true
bot.run("INSERT TOKEN", bot = False)
