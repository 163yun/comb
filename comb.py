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


def get_containers(token):
    headers = {'Content-type': 'application/json',
               'Authorization': 'Token {}'.format(token)}
    r = requests.get(ENV + '/api/v1/containers', headers=headers)
    result_json = json.loads(r.text)
    return result_json


def parse_containers_info(containers_result_json):
    all_containers_metadata_list = []
    for containers in containers_result_json['containers']:
        container_id = containers['id']
        container_name = containers['name']
        container_status = containers['status']
        container_public_ip = containers['public_ip']
        container_image_id = containers['image_id']

        this_container_metadata_list = [container_id, container_name, container_status, container_public_ip,
                                        container_image_id]
        all_containers_metadata_list.append(this_container_metadata_list)
    return all_containers_metadata_list


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


def check_user_container(app_key, app_secret):
    token = get_token(app_key, app_secret)
    container_result_json = get_containers(token)
    all_container_list = parse_containers_info(container_result_json)

    headers = ["id", "name", "status", "public_ip", "image_id"]
    tabulate_print_info(headers, all_container_list)


if __name__ == '__main__':
    # check_user_image(ACCESS_KEY, ACCESS_SECRET)
    check_user_container(ACCESS_KEY, ACCESS_SECRET)
