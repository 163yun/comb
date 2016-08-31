#!/usr/bin/env python
# encoding: utf-8

import json

import requests
from tabulate import tabulate
import click


# curl  'http://10.180.2.112:9800//networks/067d4c55e93e42eca837d1c7a1a74ce8/vxlan' -X GET \
# -H "Accept: application/json" -H "X-Auth-Token: 8b9a419ffcc64926b4ae6a4337c0155c"   |jq

# user token
HEADERS = {'Content-type': 'application/json'}
ENV = 'https://open.c.163.com'

ACCESS_KEY = '07ed767760f74d8a868071144d1048e8'
ACCESS_SECRET = 'd965faa27f794e588c412ad90b6340fc'


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


def get_images(token):
    headers = {'Content-type': 'application/json',
               'Authorization': 'Token {}'.format(token)}
    r = requests.get(ENV + '/api/v1/containers/images', headers=headers)
    result_json = json.loads(r.text)
    return result_json


def parse_images_info(image_result_json):
    all_image_metadata_list = []
    for custom_image in image_result_json['custom_images']:
        custom_image_id = custom_image['id']
        custom_image_name = custom_image['name']
        custom_image_tag = custom_image['tag']

        this_port_metadata_list = [custom_image_id, custom_image_name, custom_image_tag]
        all_image_metadata_list.append(this_port_metadata_list)

    for public_image in image_result_json['public_images']:
        public_image_id = public_image['id']
        public_image_name = public_image['name']
        public_image_tag = public_image['tag']

        this_port_metadata_list = [public_image_id, public_image_name, public_image_tag]
        all_image_metadata_list.append(this_port_metadata_list)

    return all_image_metadata_list


def tabulate_print_info(headers, result_metadata_list):
    print tabulate(result_metadata_list, headers, tablefmt="psql", stralign="left", numalign="text")


def check_user_image(app_key, app_secret):
    token = get_token(app_key, app_secret)
    image_result_json = get_images(token)
    all_image_list = parse_images_info(image_result_json)

    headers = ["id", "name", "tag"]
    tabulate_print_info(headers, all_image_list)


if __name__ == '__main__':
    check_user_image(ACCESS_KEY, ACCESS_SECRET)

