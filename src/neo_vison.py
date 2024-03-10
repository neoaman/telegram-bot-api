import os
import google.generativeai as genai
from utility import read_telegram_image
from utility.schema import TRequest
from utility.send_message import edit_send_text

genai.configure(api_key=os.environ["GOOGLE_GEMINI_API"])
model_vision = genai.GenerativeModel('gemini-pro-vision')
model_text = genai.GenerativeModel('gemini-pro')

class GenAI:

    def __init__(self,trequest:TRequest,message_id:int):
        self.trequest = trequest
        self.model = model_vision
        self.vision = True
        self.img_index = -1 # 0,1,2,3
        self.token_id = "BOT_NEO_VISON_TOKEN"
        self.chat_id = trequest.message.chat.id
        self.message_id = message_id
        if not trequest.message.photo:
            self.vision = False
            self.model = model_text 

    def update_message(self,message):
        edit_send_text(self.token_id,self.chat_id,message,self.message_id)


    def prepare_payload(self):
        self.update_message("Processing query ...")
        if self.vision:
            self.update_message("Processing Image ...")
            image_id = self.trequest.message.photo[self.img_index].file_id 
            self.image = read_telegram_image(file_id=image_id,token_id=self.token_id)
            self.text = self.trequest.message.caption
        else:
            self.image = ""
            self.text = self.trequest.message.text 
        self.content = [self.text,self.image]
        


    def get_response(self):
        self.update_message("Getting response ...")
        response = self.model.generate_content(self.content)
        return response.text

    def __call__(self):
        self.prepare_payload()
        response = self.get_response()
        self.update_message(response)
        return response

