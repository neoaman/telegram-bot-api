from fastapi import FastAPI, Body, Request, Depends, HTTPException

# LOCAL
from utility.schema import TRequest
from utility.send_message import send_text, edit_send_text
from src.neo_vison import GenAI
from utility.decorator import auth


app = FastAPI()


@app.post("/neovison")
@auth(bot_id="BOT_NEO_VISON_TOKEN")
def neo_vision_ai(trequest:TRequest,bot_id:str,chat_id:int):
    if not chat_id < 0: # If chatting in a group
        _,message_id = send_text(bot_id,chat_id,"Please Wait ...")
        if trequest.message and not trequest.message.forward_date:
            response = GenAI(trequest,message_id)()
            print(response)
        else:
            print("Unprocessable")

@app.post("/neobucket")
def read_item(trequest: TRequest):
    response = trequest.json()
    print(response)

    return "Done"

@app.post("/neobuckets")
async def read_item(trequest: Request):
    response = await trequest.json()
    print(response)
    return "Done"