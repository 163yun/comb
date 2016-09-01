#!/usr/bin/env python
# encoding: utf-8

import json

import requests
from tabulate import tabulate
import click

# user token
HEADERS = {'Content-type': 'application/json'}
ENV = 'https://open.c.163.com'

ACCESS_KEY = '07ed767760f74d8a868071144d1048e8'
ACCESS_SECRET = 'd965faa27f794e588c412ad90b6340fc'


def json_tabulate(json, json_key_list, headers_list):
    # second_key_list is headers
    # first key list is the list prepared to parse
    tabulate_data_list = []

    for key in json_key_list:
        for result in json[key]:
            result_list = {}
            this_result_list = []
            for header in headers_list:
                result_list[header] = result[header]
                this_result_list.append(result_list[header])

            tabulate_data_list.append(this_result_list)

    headers = headers_list
    return headers, tabulate_data_list


def single_json_tabulate(json, json_key_list):
    tabulate_data_list = []

    for key in json_key_list:
        result_list = {key: json[key]}
        tabulate_data_list.append([key, result_list[key]])

    headers = ["Field", "Value"]
    return headers, tabulate_data_list


def get_token(app_key, app_secret):
    headers = {'Content-type': 'application/json'}
    post_data = {
        "app_key": app_key,
        "app_secret": app_secret,
    }
    post_data_json = json.dumps(post_data)

    r = requests.post(ENV + '/api/v1/token', data=post_data_json, headers=headers)
    result_json = json.loads(r.text)
    token = result_json['token']
    return token


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


def get_repositories(token):
    headers = {'Content-type': 'application/json',
               'Authorization': 'Token {}'.format(token)}
    r = requests.get(ENV + '/api/v1/repositories', headers=headers)
    result_json = json.loads(r.text)
    return result_json


def tabulate_print_info(headers, result_metadata_list):
    print tabulate(result_metadata_list, headers, tablefmt="psql", stralign="left", numalign="text")


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
    json_key_list = ["id", "name", "status","bandwidth","public_ip","image_id"]
    headers, tabulate_data_list = single_json_tabulate(container_result_json, json_key_list)
    tabulate_print_info(headers, tabulate_data_list)


def do_container_list(app_key, app_secret):
    token = get_token(app_key, app_secret)
    container_result_json = get_containers(token)

    headers = ["id", "name", "status", "public_ip", "image_id"]
    json_key_list = ["containers"]
    headers, tabulate_data_list = json_tabulate(container_result_json, json_key_list, headers)
    tabulate_print_info(headers, tabulate_data_list)


def do_repositories_list(app_key, app_secret):
    token = get_token(app_key, app_secret)
    repositories_result_json = get_repositories(token)

    headers = ["repo_id", "repo_name", "created_at"]
    json_key_list = ["repositories"]
    headers, tabulate_data_list = json_tabulate(repositories_result_json, json_key_list, headers)
    tabulate_print_info(headers, tabulate_data_list)


if __name__ == '__main__':
    # do_container_list(ACCESS_KEY, ACCESS_SECRET)
    # do_repositories_list(ACCESS_KEY, ACCESS_SECRET)
    do_container_show(ACCESS_KEY,ACCESS_SECRET,"347339")