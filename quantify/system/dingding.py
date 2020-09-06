# encoding: utf-8
import requests
import json
from data.author import dingding_token

def msg(text):
    json_text = {
        "msgtype": "text",
        "at": {
            "atMobiles": [
                "11111"
            ],
            "isAtAll": False
        },
        "text": {
            "content": text
        }
    }
    return json_text


def dingding_warn(text):
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    api_url = "https://oapi.dingtalk.com/robot/send?access_token=%s" % dingding_token 
    json_text = msg(text)
    requests.post(api_url, json.dumps(json_text), headers=headers).content
    


if __name__ == '__main__':
    pass