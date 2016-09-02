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


def get_container_info(token, container_id):
    headers = {'Content-type': 'application/json',
               'Authorization': 'Token {}'.format(token)}
    r = requests.get(ENV + '/api/v1/containers/{container_id}'.format(container_id=container_id), headers=headers)
    result_json = json.loads(r.text)
    return result_json


def get_container_flow(token, container_id):
    headers = {'Content-type': 'application/json',
               'Authorization': 'Token {}'.format(token)}
    r = requests.get(ENV + '/api/v1/containers/{container_id}/flow'.format(container_id=container_id), headers=headers)
    result_json = json.loads(r.text)
    return result_json


def delete_container(token, container_id):
    headers = {'Content-type': 'application/json',
               'Authorization': 'Token {}'.format(token)}
    r = requests.delete(ENV + '/api/v1/containers/{container_id}'.format(container_id=container_id), headers=headers)

    return r.status_code


def restart_container(token, container_id):
    headers = {'Content-type': 'application/json',
               'Authorization': 'Token {}'.format(token)}
    r = requests.put(ENV + '/api/v1/containers/{container_id}/actions/restart'.format(container_id=container_id),
                     headers=headers)

    return r.status_code


def save_container_to_images(token, container_id):
    headers = {'Content-type': 'application/json',
               'Authorization': 'Token {}'.format(token)}
    r = requests.post(ENV + '/api/v1/containers/{container_id}/tag'.format(container_id=container_id),
                      headers=headers)

    result_json = json.loads(r.text)
    return result_json


def create_container(token):
    headers = {'Content-type': 'application/json',
               'Authorization': 'Token {}'.format(token)}
    post_data = {
        "charge_type": 1,
        "spec_id": 10,
        "image_type": 1,
        "image_id": 10029,
        "name": "test_name",
        "desc": "desc",
        "ssh_key_ids": "",
        "env_var": "{}",
        "use_public_network": 1,
        "network_charge_type": 1,
        "bandwidth": 100
    }
    post_data_json = json.dumps(post_data)
    print post_data_json
    r = requests.post(ENV + '/api/v1/containers',
                      headers=headers, data=post_data_json)

    result_json = json.loads(r.text)
    print result_json
    return result_json


def get_containers_list(token):
    headers = {'Content-type': 'application/json',
               'Authorization': 'Token {}'.format(token)}
    r = requests.get(ENV + '/api/v1/containers', headers=headers)
    result_json = json.loads(r.text)
    return result_json


@click.group()
def container(**kwargs):
    # print("This method has these arguments: " + str(kwargs))
    pass


@container.command("container-image-list")
@click.option('--app_key', default=ACCESS_KEY, help='app_key')
@click.option('--app_secret', default=ACCESS_SECRET, help='app_secret')
def do_container_image_list(app_key, app_secret):
    token = get_token(app_key, app_secret)
    image_result_json = get_container_images(token)

    headers = ["id", "name", "tag"]
    json_key_list = ["custom_images", "public_images"]
    headers, tabulate_data_list = multi_column_json_tabulate(image_result_json, json_key_list, headers)
    tabulate_print_info(headers, tabulate_data_list)


@container.command("container-show")
@click.option('--app_key', default=ACCESS_KEY, help='app_key')
@click.option('--app_secret', default=ACCESS_SECRET, help='app_secret')
@click.argument('container_id')
def do_container_show(app_key, app_secret, container_id):
    token = get_token(app_key, app_secret)
    container_result_json = get_container_info(token, container_id)

    json_key_list = ["id", "bandwidth", "charge_type", "created_at", "desc", "env_var", "image_id", "name",
                     "network_charge_type", "private_ip", "public_ip", "replicas", "spec_id", "ssh_key_ids", "status",
                     "updated_at", "use_public_network", ]
    headers, tabulate_data_list = two_columns_json_tabulate(container_result_json, json_key_list)
    tabulate_print_info(headers, tabulate_data_list)


@container.command("container-flow")
@click.option('--app_key', default=ACCESS_KEY, help='app_key')
@click.option('--app_secret', default=ACCESS_SECRET, help='app_secret')
@click.argument('container_id')
def do_get_container_flow(app_key, app_secret, container_id):
    token = get_token(app_key, app_secret)
    container_result_json = get_container_flow(token, container_id)

    json_key_list = ["container_up_flow", "container_down_flow"]
    headers, tabulate_data_list = two_columns_json_tabulate(container_result_json, json_key_list)
    tabulate_print_info(headers, tabulate_data_list)


@container.command("container-to-image")
@click.option('--app_key', default=ACCESS_KEY, help='app_key')
@click.option('--app_secret', default=ACCESS_SECRET, help='app_secret')
@click.argument('container_id')
def do_save_container_to_images(app_key, app_secret, container_id):
    token = get_token(app_key, app_secret)
    container_result_json = save_container_to_images(token, container_id)

    json_key_list = ["repo_name", "tag"]
    headers, tabulate_data_list = two_columns_json_tabulate(container_result_json, json_key_list)
    tabulate_print_info(headers, tabulate_data_list)


@container.command("container-delete")
@click.option('--app_key', default=ACCESS_KEY, help='app_key')
@click.option('--app_secret', default=ACCESS_SECRET, help='app_secret')
@click.argument('container_id')
def do_delete_container(app_key, app_secret, container_id):
    token = get_token(app_key, app_secret)
    delete_container(token, container_id)


@container.command("container-restart")
@click.option('--app_key', default=ACCESS_KEY, help='app_key')
@click.option('--app_secret', default=ACCESS_SECRET, help='app_secret')
@click.argument('container_id')
def do_restart_container(app_key, app_secret, container_id):
    token = get_token(app_key, app_secret)
    restart_container(token, container_id)


@container.command("container-list")
@click.option('--app_key', default=ACCESS_KEY, help='user tenantId')
@click.option('--app_secret', default=ACCESS_SECRET, help='user tenantId')
def do_container_list(app_key, app_secret):
    token = get_token(app_key, app_secret)
    container_result_json = get_containers_list(token)

    headers = ["id", "name", "status", "public_ip", "image_id"]
    json_key_list = ["containers"]
    headers, tabulate_data_list = multi_column_json_tabulate(container_result_json, json_key_list, headers)
    tabulate_print_info(headers, tabulate_data_list)


def tabulate_print_info(headers, result_metadata_list):
    print tabulate(result_metadata_list, headers, tablefmt="psql", stralign="left", numalign="left")


if __name__ == '__main__':
    token = get_token(ACCESS_KEY, ACCESS_SECRET)
    create_container(token)