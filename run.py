#!/bin/python

import os
import discord

from datetime import datetime
from functions import responses
from dotenv import load_dotenv

async def send_message(message, user_message, is_private):
    # Respond
    try:
        response = responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as err:
        message = f"{str(err)}"
        print(message)

def run_discord_bot():
    # Import environmental variables / Import API Token
    load_env = load_dotenv('.env')
    TOKEN = os.environ.get("TOKEN")
    BOT_ID = os.environ.get("BOT_ID")

    # Configure intents for Discord
    intents = discord.Intents.default()
    intents.message_content = True

    # Create client
    client = discord.Client(intents=intents)

    # On Ready Self Check
    @client.event
    async def on_ready():
        timestamp = datetime.now()
        message = f"[{timestamp}] [BOT] {client.user} is now running!"
        print(message)

    # On Message
    @client.event
    async def on_message(message):
        # Grab message data
        username = str(message.author)
        user_msg = str(message.content)
        channel = str(message.channel)
        timestamp = datetime.now()

        # If the message is from self
        if message.author == client.user:
            print(f"[{timestamp}] [{channel}] {username}: {user_msg}")
            return
        else:
            print(f"[{timestamp}] [{channel}] {username}: {user_msg}")
        
        if user_msg[0] == "?":
            user_msg = user_msg[1:]
            await send_message(message, user_msg, is_private = True)
        elif BOT_ID in user_msg:
            user_msg = user_msg.replace(BOT_ID, "")
            await send_message(message, user_msg, is_private = False)

    client.run(TOKEN)
        
if __name__ == "__main__":
    run_discord_bot()