
if __name__ == '__main__':
	from discord_bot import Bot
	from utils.discord import DiscordConfig
	from utils import get_env
	bot = Bot(config=DiscordConfig())
	bot.run(get_env('DISCORD_BOT_TOKEN', None))
	#from discord_bot import main
	#main()