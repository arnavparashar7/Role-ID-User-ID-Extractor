import discord
from discord.ext import commands
import csv

# Replace 'YOUR_BOT_TOKEN' with your bot's token
TOKEN = 'TokenID'
# Replace 'ROLE_ID' with the ID of the role you want to target (as an integer)
ROLE_ID = RoleID  # Example role ID
# Replace 'GUILD_ID' with the ID of the server you want to target (as an integer)
GUILD_ID = ServerID  # Example guild ID

intents = discord.Intents.default()
intents.members = True  # Enable members intent

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    guild = bot.get_guild(GUILD_ID)  # Get the specific guild by ID

    if guild:
        role = guild.get_role(ROLE_ID)
        if role:
            members_with_role = [member for member in guild.members if role in member.roles]
            with open('members_with_role.csv', mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['Server ID', 'Username', 'ID'])  # Write header
                for member in members_with_role:
                    writer.writerow([guild.id, member.name, member.id])  # Write server and member details
            print(f'Successfully written {len(members_with_role)} members to members_with_role.csv')
        else:
            print(f'Role with ID "{ROLE_ID}" not found in guild "{GUILD_ID}".')
    else:
        print(f'Guild with ID "{GUILD_ID}" not found.')

# Run the bot
bot.run(TOKEN)
