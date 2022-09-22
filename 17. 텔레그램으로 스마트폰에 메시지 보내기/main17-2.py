import telegram

token = ''
id = ""

bot = telegram.Bot(token)
bot.send_message(chat_id=id, text="파이썬으로 보내는 메시지 입니다.")