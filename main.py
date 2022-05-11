import nextcord
import nextcord as discord
from nextcord.ui import Button, View
from nextcord.ext import commands
import os
#import music
intents = nextcord.Intents.all()
client = commands.Bot(command_prefix="?", case_insensitive=True, intents=intents)

@client.event
async def on_ready():
	await client.get_channel(959112198578393148).send('🟢 WaterMod is online')
	print(f'Logged in as {client.user.name}')
	await client.change_presence(status=nextcord.Status.dnd, activity=nextcord.Game(name=f"Playing /help with {len(client.users)} users in {len(client.guilds)} servers"))

# making file changes for a test
  
@client.slash_command(
name="purge",
description="Clears The Amount Of Messages Given"
)
@commands.has_permissions(manage_messages=True)
async def purge(inter: nextcord.Interaction, amount: int = nextcord.SlashOption(name="amount", description = "The Number Of Messages To Delete")):
    await inter.response.send_message(f"Deleting {amount} messages.")
    await inter.channel.purge(limit=amount+1)
    await inter.channel.send("All the messages were deleted!")

@client.slash_command(
  name = "kick",
  description = "Kick a user from your server."
)
async def kick(
  inter : nextcord.Interaction,
  member : nextcord.Member = nextcord.SlashOption(
	name="member",
    description="The member you would like to kick from the server"),
    reason : str = "No reason provided"
):
  try:
    em1 = discord.Embed(title="Kicked", description = f"{member.name} has been kicked from the server because : {reason}", color = discord.Color.random())
    
    em2 = nextcord.Embed(title="Kicked", description = f"You have been kicked from `{inter.guild.name}` caause : {reason}")

    await inter.response.send_message(embed=em1)
    await member.send(embed=em2)
    await member.kick(reason=reason)
    
  except Exception as e:
    raise e
    
"""
@kick.error
async def info_error(inter, error):
    if isinstance(error, commands.MissingPermissions):
        await inter.response.send_message("You cannot kick members cause you don't have the appropriate permissions.")
        await inter.response.send_message(embed=discord.Embed(title="Bot is missing permissions", description="The bot is missing required permissions to execute the command."))

"""

@client.slash_command(name="ban", description="Bans a user")
async def ban(inter : nextcord.Interaction, member : nextcord.Member = nextcord.SlashOption(name="member", description="The member to ban"), reason : str = nextcord.SlashOption(name="reason", description="Reason to ban")):
	try:
		embed = nextcord.Embed(title="Banned", description=f"{member} was banned. reason: {reason}", colour=0xff0000)
		await inter.response.send_message(embed=embed)
		await member.ban(reason=reason)
	except Exception as e:
		raise e

@client.slash_command(name="unban", description="unban a user")
async def unban(inter : nextcord.Interaction, user : nextcord.User = nextcord.SlashOption(name="user", description="The user to unban")):
	user = client.get_user(user)
	bans = await inter.guild.bans()
	for ban in bans:
		if ban.user.id == user.id:
			await inter.guild.unban(user=user)
			await inter.response.send_message("Unbanned")

@client.slash_command(
  name="poll",
  description="Create a poll"
)
async def pollz(
  inter: nextcord.Interaction,
  message: str = nextcord.SlashOption(description="Please enter a description for the poll and separate them by adding an 'or'")
):
  channel = inter.channel
  try:
	  op1, op2 = message.split("or")
	  txt = f"React with :white_check_mark: for {op1} or :x: for {op2}"
  except:
    await inter.response.send_message("Correct syntax : {choice1} or {choice2} , and don't add these brackets they are just for justification.")
    return

  embed = discord.Embed(title="Poll", description = txt, color=discord.Color.random())
  await inter.response.send_message(embed=embed)
  message = await inter.original_message()
  await message.add_reaction("✅")
  await message.add_reaction("❌")
   

      

#client.add_cog(music(client))

    
def test():
  return """
  🌊 **/purge** - "/purge (the number of messages you want to purge)" 
  """

@client.slash_command(
  name ="help",
  description="help commands"
)
async def help_command(
  inter: nextcord.Interaction
):
  button1 = Button(label="Moderation", style = discord.ButtonStyle.green, emoji = "🤖")

  async def button1_callback(interaction):
    await interaction.response.send_message(embed=discord.Embed(title = "Moderation", description=test(), color= discord.Color.random()), ephemeral = True)

  button1.callback = button1_callback
  
  view = View()
  view.add_item(button1)


  await inter.response.send_message("test", view=view)

client.run(os.getenv('token'))
