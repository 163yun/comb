__author__ = 'hzhuangzhexiao'

import json
import ConfigParser

import requests


conf = ConfigParser.ConfigParser()
conf.read("auth.conf")

COMB_OPENAPI = conf.get("section", "COMB_OPENAPI")
ACCESS_KEY = conf.get("section", "ACCESS_KEY")
ACCESS_SECRET = conf.get("section", "ACCESS_KEY")


def get_token(app_key, app_secret):
    headers = {'Content-type': 'application/json'}
    post_data = {
        "app_key": app_key,
        "app_secret": app_secret,
    }
    post_data_json = json.dumps(post_data)

    r = requests.post(COMB_OPENAPI + '/api/v1/token', data=post_data_json, headers=headers)
    result_json = json.loads(r.text)
    token = result_json['token']
    return token



