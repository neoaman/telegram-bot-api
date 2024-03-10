from .schema import TRequest
from .send_message import send_text
import traceback


def auth(bot_id):
    def verify_user_info(func):
        def wrapper_func(trequest:TRequest,chat_id=None):
            if trequest.message:
                chat_id = trequest.message.chat.id
            elif trequest.channel_post:
                chat_id = trequest.channel_post.chat.id
            
            if chat_id in [923873283,-1002121422688, -1001499379403]:
                try:
                    func(trequest,bot_id,chat_id)
                except Exception as e:
                    response = f"*Error* !\n*Traceback* \n```text \n{traceback.format_exc()}``` \n*Payload* \n```json\n{trequest.json()}\n```\n ||{e}||"
                    send_text(token_id=bot_id,chat_id=923873283,text=response)
                    send_text(token_id=bot_id,chat_id=chat_id,text="I Apologize for the Inconvenience, please try again or report to my creator t.me/neoaman")
            else:
                send_text(token_id=bot_id,chat_id=chat_id,text="Please contact t.me/neoaman for access")
                send_text(token_id=bot_id,chat_id=923873283,text=f"Please check and Grant access to id :{chat_id}")
                return None
        return wrapper_func
    return verify_user_info