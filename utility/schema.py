from pydantic import BaseModel
from typing import Union, List

class TPhoto(BaseModel):
    file_id: str
    file_unique_id: str
    file_size: int
    width: int
    height: int
    
class TDocument(BaseModel):
    filename: str
    mime_type: str
    file_id: str
    file_unique_id: str
    file_size: int

class TMusic(BaseModel):
    duration: int
    filename: str
    mime_type: str
    title: str
    performer: str
    file_id: str
    file_unique_id: str
    file_size: int

class TVideo(BaseModel):
    duration: int
    width: int
    height: int
    mime_type: str
    thumbnail: Union[TPhoto,None] = None
    thumb: Union[TPhoto,None] = None
    file_id: str
    file_unique_id: str
    file_size: int

class TChat(BaseModel):
    id: int
    first_name: Union[str,None] = None
    last_name: Union[str,None] = None
    username: Union[str,None] = None
    title: Union[str,None] = None
    type: str

class TMessage(BaseModel):
    message_id: int
    chat: TChat
    forward_origin: Union[dict,None] = None
    forward_from_chat: Union[dict,None] = None
    forward_from_message_id: Union[int,None] = None
    forward_date: Union[int,None] = None
    date: int
    photo: Union[List[TPhoto],None] = None
    video: Union[TVideo,None] = None
    document: Union[TDocument,None] = None
    music: Union[TMusic,None] = None
    caption: Union[str,None] = " "
    text: Union[str,None] = None
    location: Union[dict,None] = None

class TRequest(BaseModel):
    update_id: int
    message: Union[TMessage,None] = None
    channel_post: Union[TMessage,None] = None
