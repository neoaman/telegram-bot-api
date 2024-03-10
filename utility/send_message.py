import requests
import os


def send_text(token_id,chat_id,text):
    bot_api_sandessage = f"https://api.telegram.org/bot{os.environ[token_id]}/sendMessage"
    payload = {'chat_id':chat_id,'text': text, "parse_mode":"Markdown"}
    response = requests.request("POST", bot_api_sandessage, headers={}, data=payload)
    message_id = response.json()["result"]["message_id"]
    return response,message_id

def edit_send_text(token_id,chat_id,text,message_id):
    bot_api_sandessage = f"https://api.telegram.org/bot{os.environ[token_id]}/editMessageText"
    payload = {'chat_id':chat_id,'text': text, "parse_mode":"Markdown","message_id":message_id}
    response = requests.request("POST", bot_api_sandessage, headers={}, data=payload)
    return response

# def send_image()
