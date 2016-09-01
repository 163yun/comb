import requests
import json
from utils import *
from json_tabulate import *

def get_app_images(token):
    headers = {'Content-type': 'application/json',
               'Authorization': 'Token {}'.format(token)}
    r = requests.get(ENV + '/api/v1/apps/images', headers=headers)
    result_json = json.loads(r.text)
    return result_json

def do_app_image_list(app_key, app_secret):
    token = get_token(app_key, app_secret)
    image_result_json = get_app_images(token)

    headers = ["id", "name", "tag"]
    json_key_list = ["custom_images", "public_images"]
    headers, tabulate_data_list = multi_column_json_tabulate(image_result_json, json_key_list, headers)
    tabulate_print_info(headers, tabulate_data_list)



def tabulate_print_info(headers, result_metadata_list):
    print tabulate(result_metadata_list, headers, tablefmt="psql", stralign="left", numalign="text")


if __name__ == '__main__':
    do_app_image_list(ACCESS_KEY, ACCESS_SECRET)



