import requests
import json
from utils import *
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


def get_container_flow(token, containerId):
    headers = {'Content-type': 'application/json',
               'Authorization': 'Token {}'.format(token)}
    r = requests.get(ENV + '/api/v1/containers/{containerId}/flow'.format(containerId=containerId), headers=headers)
    result_json = json.loads(r.text)
    return result_json


def delete_container(token, containerId):
    headers = {'Content-type': 'application/json',
               'Authorization': 'Token {}'.format(token)}
    r = requests.delete(ENV + '/api/v1/containers/{containerId}'.format(containerId=containerId), headers=headers)

    return r.status_code


def restart_container(token, containerId):
    headers = {'Content-type': 'application/json',
               'Authorization': 'Token {}'.format(token)}
    r = requests.put(ENV + '/api/v1/containers/{containerId}/actions/restart'.format(containerId=containerId),
                     headers=headers)

    return r.status_code


def save_container_to_images(token, containerId):
    headers = {'Content-type': 'application/json',
               'Authorization': 'Token {}'.format(token)}
    r = requests.post(ENV + '/api/v1/containers/{containerId}/tag'.format(containerId=containerId),
                      headers=headers)

    result_json = json.loads(r.text)
    return result_json


def get_containers_list(token):
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
    headers, tabulate_data_list = multi_column_json_tabulate(image_result_json, json_key_list, headers)
    tabulate_print_info(headers, tabulate_data_list)


def do_container_show(app_key, app_secret, containerId):
    token = get_token(app_key, app_secret)
    container_result_json = get_container_info(token, containerId)

    json_key_list = ["id", "name", "status", "bandwidth", "public_ip", "image_id"]
    headers, tabulate_data_list = two_columns_json_tabulate(container_result_json, json_key_list)
    tabulate_print_info(headers, tabulate_data_list)


def do_get_container_flow(app_key, app_secret, containerId):
    token = get_token(app_key, app_secret)
    container_result_json = get_container_flow(token, containerId)

    json_key_list = ["container_up_flow", "container_down_flow"]
    headers, tabulate_data_list = two_columns_json_tabulate(container_result_json, json_key_list)
    tabulate_print_info(headers, tabulate_data_list)


def do_save_container_to_images(app_key, app_secret, containerId):
    token = get_token(app_key, app_secret)
    container_result_json = save_container_to_images(token, containerId)

    json_key_list = ["repo_name", "tag"]
    headers, tabulate_data_list = two_columns_json_tabulate(container_result_json, json_key_list)
    tabulate_print_info(headers, tabulate_data_list)


def do_delete_container(app_key, app_secret, containerId):
    token = get_token(app_key, app_secret)
    delete_container(token, containerId)


def do_restart_container(app_key, app_secret, containerId):
    token = get_token(app_key, app_secret)
    restart_container(token, containerId)


def do_container_list(app_key, app_secret):
    token = get_token(app_key, app_secret)
    container_result_json = get_containers_list(token)

    headers = ["id", "name", "status", "public_ip", "image_id"]
    json_key_list = ["containers"]
    headers, tabulate_data_list = multi_column_json_tabulate(container_result_json, json_key_list, headers)
    tabulate_print_info(headers, tabulate_data_list)


def tabulate_print_info(headers, result_metadata_list):
    print tabulate(result_metadata_list, headers, tablefmt="psql", stralign="left", numalign="text")


if __name__ == '__main__':
    do_container_list(ACCESS_KEY, ACCESS_SECRET)
    # do_repositories_list(ACCESS_KEY, ACCESS_SECRET)
    do_container_show(ACCESS_KEY, ACCESS_SECRET, "193887")
    do_get_container_flow(ACCESS_KEY, ACCESS_SECRET, "193887")
