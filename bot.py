from pyrogram import Client, filters
import random

# Create a Pyrogram client
app = Client("prank_bot")

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
]

# Define a function to handle incoming messages
@app.on_message(filters.private)
async def handle_message(client, message):
    # Choose a random prank message
    prank_message = random.choice(prank_messages)
    
    # Send the prank message to the user
    await message.reply_text(prank_message)

# Run the client
app.run()
