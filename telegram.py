import requests

class Telegram: 

    def __init__(self, token):
        self.token = token
    
    def __telegram(self, token, method, payload = {}):
        return requests.get('https://api.telegram.org/bot' + \
                self.token + method, params = payload).json()
    
    def getMe(self):
        return self.__telegram(self.token, '/getMe')

    def getUpdates(self, offset, timeout = 60):
        return self.__telegram(self.token, '/getUpdates',
                {'timeout' : timeout, 'offset' : offset})
        
    def sendMessage(self, recipient, message, parse_mode = 'HTML'):
        return self.__telegram(self.token, '/sendMessage', 
                {'chat_id' : recipient, 'text' : message, 
                    'parse_mode' : parse_mode})

    def listen(self, callback, parse_mode = 'HTML', offset = 0):
        while True:
            request = self.getUpdates(offset)
            if not (request['ok'] and request['result']): continue

            for result in request['result']:
                message = result['message']['text'] 
                chat_id = result['message']['chat']['id']

                callback(self, message, chat_id)

                offset = result['update_id'] + 1
