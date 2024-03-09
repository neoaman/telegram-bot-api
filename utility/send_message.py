import requests
import os


def send_text(token_id,chat_id,text):
    bot_api_sandessage = f"https://api.telegram.org/bot{os.environ[token_id]}/sendMessage"
    payload = {'chat_id':chat_id,'text': text}
    response = requests.request("POST", bot_api_sandessage, headers={}, data=payload)
    return response
            
