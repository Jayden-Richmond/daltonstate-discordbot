import discord
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID").strip()
bot = discord.Client(intents=intents)

print(f"Loaded DISCORD_TOKEN: {DISCORD_TOKEN[:10]}. . .")
print(f"Loaded Channel_ID: {CHANNEL_ID}")

@bot.event
async def on_ready():
    guild_count = 0

    for guild in bot.guilds:

        print(f"- {guild.id} (name: {guild.name})")
        

        guild_count = guild_count + 1

    print("Roady is in " + str(guild_count) + " guilds.")

    for guild in bot.guilds:
        print(f"Guild: {guild.name} (ID: {guild.id})")
        for channel in guild.channels:
            print(f"  Channel: {channel.name} (ID: {channel.id}, Type: {channel.type})")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return


    if message.content == "hello":
        await message.channel.send("hey dirtbag")

@bot.event
async def on_member_join(member):
    print(f"Member {member.name} joined.")
    print(f"Fetching channel with ID: {CHANNEL_ID}")

    channel = bot.get_channel(int(CHANNEL_ID))
    if channel:
        print(f"Channel found: {channel.name} (ID: {channel.id}), sending message.")
        await channel.send("LEAVE NOW COMMIE!")
    
    else:
        print("channel not found. Checking available channels.")
        for guild in bot.guilds:
            for ch in guild.channels:
                print(f"- {ch.name} (ID: {ch.id}, Type: {ch.type})")
                if ch.id == CHANNEL_ID:
                    print("Direct match found with channel listing.")

    


bot.run(DISCORD_TOKEN)
