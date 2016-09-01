
import requests
from utils import  *
import json
from json_tabulate import *

def get_repositories(token):
    headers = {'Content-type': 'application/json',
               'Authorization': 'Token {}'.format(token)}
    r = requests.get(ENV + '/api/v1/repositories', headers=headers)
    result_json = json.loads(r.text)
    return result_json

def do_repositories_list(app_key, app_secret):
    token = get_token(app_key, app_secret)
    repositories_result_json = get_repositories(token)

    headers = ["repo_id", "repo_name", "created_at"]
    json_key_list = ["repositories"]
    headers, tabulate_data_list = json_tabulate(repositories_result_json, json_key_list, headers)
    tabulate_print_info(headers, tabulate_data_list)

