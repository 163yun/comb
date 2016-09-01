import requests
import json
from utils import  *
from json_tabulate import *


def get_container_images(token):
    headers = {'Content-type': 'application/json',
               'Authorization': 'Token {}'.format(token)}
    r = requests.get(ENV + '/api/v1/containers/images', headers=headers)
    result_json = json.loads(r.text)
    return result_json


def get_container_info(token, containerId):
    headers = {'Content-type': 'application/json',
               'Authorization': 'Token {}'.format(token)}
    r = requests.get(ENV + '/api/v1/containers/{containerId}'.format(containerId=containerId), headers=headers)
    result_json = json.loads(r.text)
    return result_json


def get_containers(token):
    headers = {'Content-type': 'application/json',
               'Authorization': 'Token {}'.format(token)}
    r = requests.get(ENV + '/api/v1/containers', headers=headers)
    result_json = json.loads(r.text)
    return result_json

def do_container_image_list(app_key, app_secret):
    token = get_token(app_key, app_secret)
    image_result_json = get_container_images(token)

    headers = ["id", "name", "tag"]
    json_key_list = ["custom_images", "public_images"]
    headers, tabulate_data_list = json_tabulate(image_result_json, json_key_list, headers)
    tabulate_print_info(headers, tabulate_data_list)


def do_container_show(app_key, app_secret, containerId):
    token = get_token(app_key, app_secret)
    container_result_json = get_container_info(token, containerId)

    headers = ["id", "name", "tag"]
    json_key_list = ["id", "name", "status", "bandwidth", "public_ip", "image_id"]
    headers, tabulate_data_list = single_json_tabulate(container_result_json, json_key_list)
    tabulate_print_info(headers, tabulate_data_list)


def do_container_list(app_key, app_secret):
    token = get_token(app_key, app_secret)
    container_result_json = get_containers(token)

    headers = ["id", "name", "status", "public_ip", "image_id"]
    json_key_list = ["containers"]
    headers, tabulate_data_list = json_tabulate(container_result_json, json_key_list, headers)
    tabulate_print_info(headers, tabulate_data_list)

def tabulate_print_info(headers, result_metadata_list):
    print tabulate(result_metadata_list, headers, tablefmt="psql", stralign="left", numalign="text")