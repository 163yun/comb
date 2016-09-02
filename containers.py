import requests
import json
import click
from utils import *
from json_tabulate import *
from tabulate import tabulate


def get_container_images(token):
    headers = {'Content-type': 'application/json',
               'Authorization': 'Token {}'.format(token)}
    r = requests.get(COMB_OPENAPI + '/api/v1/containers/images', headers=headers)
    result_json = json.loads(r.text)
    return result_json


def get_container_info(token, container_id):
    headers = {'Content-type': 'application/json',
               'Authorization': 'Token {}'.format(token)}
    r = requests.get(COMB_OPENAPI + '/api/v1/containers/{container_id}'.format(container_id=container_id),
                     headers=headers)
    result_json = json.loads(r.text)
    return result_json


def get_container_flow(token, container_id):
    headers = {'Content-type': 'application/json',
               'Authorization': 'Token {}'.format(token)}
    r = requests.get(COMB_OPENAPI + '/api/v1/containers/{container_id}/flow'.format(container_id=container_id),
                     headers=headers)
    result_json = json.loads(r.text)
    return result_json


def delete_container(token, container_id):
    headers = {'Content-type': 'application/json',
               'Authorization': 'Token {}'.format(token)}
    r = requests.delete(COMB_OPENAPI + '/api/v1/containers/{container_id}'.format(container_id=container_id),
                        headers=headers)

    return r.status_code


def restart_container(token, container_id):
    headers = {'Content-type': 'application/json',
               'Authorization': 'Token {}'.format(token)}
    r = requests.put(
        COMB_OPENAPI + '/api/v1/containers/{container_id}/actions/restart'.format(container_id=container_id),
        headers=headers)

    return r.status_code


def save_container_to_images(token, container_id):
    headers = {'Content-type': 'application/json',
               'Authorization': 'Token {}'.format(token)}
    r = requests.post(COMB_OPENAPI + '/api/v1/containers/{container_id}/tag'.format(container_id=container_id),
                      headers=headers)

    result_json = json.loads(r.text)
    return result_json


def create_container(token, charge_type, spec_id, image_type, image_id, name, desc, use_public_network,
                     network_charge_type, bandwidth):
    headers = {'Content-type': 'application/json',
               'Authorization': 'Token {}'.format(token)}
    post_data = {
        "charge_type": charge_type,
        "spec_id": spec_id,
        "image_type": image_type,
        "image_id": image_id,
        "name": name,
        "desc": desc,
        "use_public_network": use_public_network,
        "network_charge_type": network_charge_type,
        "bandwidth": bandwidth
    }
    post_data_json = json.dumps(post_data)
    print post_data_json
    r = requests.post(COMB_OPENAPI + '/api/v1/containers',
                      headers=headers, data=post_data_json)

    result_json = json.loads(r.text)
    print result_json
    return result_json


def get_containers_list(token):
    headers = {'Content-type': 'application/json',
               'Authorization': 'Token {}'.format(token)}
    r = requests.get(COMB_OPENAPI + '/api/v1/containers', headers=headers)
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
    container_image_result_json = get_container_images(token)

    headers = ["id", "name", "tag"]
    json_key_list = ["custom_images", "public_images"]
    headers, tabulate_data_list = multi_column_json_tabulate(container_image_result_json, json_key_list, headers)
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
    container_flow_result_json = get_container_flow(token, container_id)

    json_key_list = ["container_up_flow", "container_down_flow"]
    headers, tabulate_data_list = two_columns_json_tabulate(container_flow_result_json, json_key_list)
    tabulate_print_info(headers, tabulate_data_list)


@container.command("container-create")
@click.option('--app_key', default=ACCESS_KEY, help='app_key')
@click.option('--app_secret', default=ACCESS_SECRET, help='app_key')
@click.option('--charge_type')
@click.option('--spec_id')
@click.option('--image_type')
@click.option('--image_id')
@click.option('--name')
@click.option('--desc', default="")
@click.option('--use_public_network', default="")
@click.option('--network_charge_type', default="")
@click.option('--bandwidth', default="")
def do_container_create(app_key, app_secret, charge_type, spec_id, image_type, image_id, name, desc, use_public_network,
                        network_charge_type, bandwidth):
    """
    container create command \n
    demo: \n 
    container-create --charge_type 1 --spec_id 1 --image_type 1 --image_id 10005 --name testNew
"""
    token = get_token(app_key, app_secret)
    create_container(token, charge_type, spec_id, image_type, image_id, name, desc, use_public_network,
                     network_charge_type, bandwidth)


@container.command("container-to-image")
@click.option('--app_key', default=ACCESS_KEY, help='app_key')
@click.option('--app_secret', default=ACCESS_SECRET, help='app_secret')
@click.argument('container_id')
def do_save_container_to_images(app_key, app_secret, container_id):
    token = get_token(app_key, app_secret)
    save_container_result_json = save_container_to_images(token, container_id)

    json_key_list = ["repo_name", "tag"]
    headers, tabulate_data_list = two_columns_json_tabulate(save_container_result_json, json_key_list)
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
    container_list_result_json = get_containers_list(token)

    headers = ["id", "name", "status", "public_ip", "image_id"]
    json_key_list = ["containers"]
    headers, tabulate_data_list = multi_column_json_tabulate(container_list_result_json, json_key_list, headers)
    tabulate_print_info(headers, tabulate_data_list)


def tabulate_print_info(headers, result_metadata_list):
    print tabulate(result_metadata_list, headers, tablefmt="psql", stralign="left", numalign="left")


if __name__ == '__main__':
    token = get_token(ACCESS_KEY, ACCESS_SECRET)
    create_container(token)