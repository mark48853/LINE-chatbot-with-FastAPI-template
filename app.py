import uvicorn
import requests
from fastapi import Request
from fastapi import FastAPI
from config import *

app = FastAPI()

@app.post("/")
async def home(request:Request):
    reply_token = request['events'][0]['replyToken'] #reply token
    callback(reply_token)
    return "OK!",200

def callback(reply_token):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'
    Auth = 'Bearer {}'.format(channel_access_token)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': Auth
    }
    data = {
        'reply_token':reply_token,
        'messages':[{
            "type": "text",
            "text": "Hello"
        }]
    }
    data = json.dumps(data) #dumps from dict to Json
    r = requests.post(LINE_API, headers, data)
    return 200