import urllib.request
import requests
import os
from pathlib import Path
from uuid import uuid4 
from PIL import Image

tmp_file_dir = Path.cwd() / "static" / "temp"

def download_file(file_url,file_name):
    urllib.request.urlretrieve(file_url,file_name)

    return None

def read_telegram_image(file_id,token_id):
    bot_api_getfile = f"https://api.telegram.org/bot{os.environ[token_id]}/getFile"
    fileinfo = requests.request("POST", bot_api_getfile, data={"file_id":file_id})
    file_path = fileinfo.json()["result"]["file_path"]
    file_url = f"https://api.telegram.org/file/bot{os.environ[token_id]}/"+file_path
    temp_path =  tmp_file_dir / str(uuid4())
    download_file(file_url,temp_path)
    image = Image.open(temp_path)
    temp_path.unlink(missing_ok=True)
    return image

