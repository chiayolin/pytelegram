from telegram import *

token = ''
Telegram(token).listen(lambda req: req['message'])
