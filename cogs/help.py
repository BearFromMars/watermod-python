import disnake
import disnake as discord 
from disnake.ext import commands
from disnake.ui import Button, View

class Help(commands.Cog):
	def __init__(self, client):
		self.client = client

def setup(client : commands.Bot):
	client.add_cog(Help(client))