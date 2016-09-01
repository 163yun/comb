import requests
import json
from utils import *
from json_tabulate import *


def get_repositories_list(token):
    headers = {'Content-type': 'application/json',
               'Authorization': 'Token {}'.format(token)}
    r = requests.get(ENV + '/api/v1/repositories', headers=headers)
    result_json = json.loads(r.text)
    return result_json


def show_repositories(token, id):
    headers = {'Content-type': 'application/json',
               'Authorization': 'Token {}'.format(token)}
    r = requests.get(ENV + '/api/v1/repositories/{}'.format(id), headers=headers)
    result_json = json.loads(r.text)
    return result_json


def do_repositories_list(app_key, app_secret):
    token = get_token(app_key, app_secret)
    repositories_result_json = get_repositories_list(token)

    headers = ["repo_id", "repo_name", "created_at"]
    json_key_list = ["repositories"]
    headers, tabulate_data_list = json_tabulate(repositories_result_json, json_key_list, headers)
    tabulate_print_info(headers, tabulate_data_list)


def do_show_repositories(app_key, app_secret, id):
    token = get_token(app_key, app_secret)
    repositories_result_json = show_repositories(token, id)

    json_key_list = ["repo_id", "repo_name", "user_name", "open_level", "detail_desc", "created_at", "updated_at"]
    headers, tabulate_data_list = single_json_tabulate(repositories_result_json, json_key_list)
    tabulate_print_info(headers, tabulate_data_list)


def tabulate_print_info(headers, result_metadata_list):
    print tabulate(result_metadata_list, headers, tablefmt="psql", stralign="left", numalign="text")


if __name__ == '__main__':
    do_repositories_list(ACCESS_KEY, ACCESS_SECRET)
    do_show_repositories(ACCESS_KEY, ACCESS_SECRET, "5331")