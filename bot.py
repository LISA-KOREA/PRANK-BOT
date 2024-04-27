from pyrogram import Client, filters
import random
import asyncio

# Add your API ID, API hash, and bot token obtained from the Telegram website
api_id = "4888076"
api_hash = "8b9b8214d84305d5ba8042c93575ea84"
bot_token = "7079010083:AAHVvDum-QVE5v855wuvWtJzL2bE-GzHCP0"

# Create a Pyrogram client
app = Client("prank_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Define a list of prank messages
prank_messages = [
    "Oops! You've been pranked! 😜",
    "Surprise! It's just a prank! 🎉",
    "Gotcha! Prank time! 🃏",
    "You're the lucky winner of a prank! 🥳",
    "This message will self-destruct in 3... 2... 1... BOOM! Just kidding 😄",
    "Congratulations! You've won a free imaginary vacation to Mars! 🚀",
    "Warning: This message contains extreme levels of prankiness! Proceed with caution. 😄",
    "You've unlocked the secret prank level! Prepare for the unexpected! 🎈",
    "You just missed the prank train! 🚂 Better luck next time! 😄",
    "Unexpected error: Prank.exe has stopped working. Just kidding! 😂",
    "Important announcement: You've been officially pranked! 📢",
    "Prank level: Expert! You're now a certified prankster! 🏆",
]

# Define a function to handle the /start command
@app.on_message(filters.command("start"))
async def start_command(client, message):
    # Send a welcome message to the user
    await message.reply_text("Welcome to the Prank Bot! Get ready to be pranked! 😄")

# Define a function to handle incoming messages
@app.on_message(filters.private)
async def handle_message(client, message):
    # Choose a random prank message
    prank_message = random.choice(prank_messages)
    
    # Send the prank message to the user
    if "BOOM" in prank_message:
        await message.reply_animation(animation="https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif")
    else:
        await message.reply_text(prank_message)

# Run the client
app.run()
