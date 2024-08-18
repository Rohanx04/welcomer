import discord
from discord.ext import commands
from flask import Flask, render_template
import threading

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

app = Flask(__name__)

# Discord bot code
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel("channel_ID")
    embed = discord.Embed(title=f"Welcome to the server, {member.name}!", color=0xFFD700)
    embed.add_field(name="Rules", value="Be sure to read the rules before you start.", inline=False)
    avatar_url = member.avatar.url if member.avatar else member.default_avatar.url
    embed.set_thumbnail(url=avatar_url)
    
    await channel.send(embed=embed)

# Web view code using Flask
@app.route('/')
def index():
    # Your web application code here
    return render_template('index.html')

def run_discord_bot():
    # Replace 'your_bot_token' with the actual token of your Discord bot.
    bot.run("process.env.token")

if __name__ == '__main__':
    # Start the Discord bot in a separate thread
    bot_thread = threading.Thread(target=run_discord_bot)
    bot_thread.start()

    # Run the Flask app in the main thread
    app.run(host='0.0.0.0', port=8080)
