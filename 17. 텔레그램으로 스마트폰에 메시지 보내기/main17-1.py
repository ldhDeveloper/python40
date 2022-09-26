import telegram

token = '5691766749:AAE5-Q35ApdXh2K-Sc_aDwfxn_JLkwWLI_k'
bot = telegram.Bot(token=token)
updates = bot.getUpdates()
for u in updates:
    print(u.message)