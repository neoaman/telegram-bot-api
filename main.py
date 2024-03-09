from fastapi import FastAPI, Body, Request

# LOCAL
from utility.schema import TRequest
from utility.send_message import send_text
from src.neo_vison import GenAI


app = FastAPI()

@app.post("/neovison")
def neo_vision_ai(trequest:TRequest):
    if trequest.message and not trequest.message.forward_date:
        response = GenAI(trequest)()
    print(response)

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