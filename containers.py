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


def get_container_info(token, containerid):
    headers = {'Content-type': 'application/json',
               'Authorization': 'Token {}'.format(token)}
    r = requests.get(ENV + '/api/v1/containers/{containerid}'.format(containerid=containerid), headers=headers)
    result_json = json.loads(r.text)
    return result_json


def get_container_flow(token, containerid):
    headers = {'Content-type': 'application/json',
               'Authorization': 'Token {}'.format(token)}
    r = requests.get(ENV + '/api/v1/containers/{containerid}/flow'.format(containerid=containerid), headers=headers)
    result_json = json.loads(r.text)
    return result_json


def delete_container(token, containerid):
    headers = {'Content-type': 'application/json',
               'Authorization': 'Token {}'.format(token)}
    r = requests.delete(ENV + '/api/v1/containers/{containerid}'.format(containerid=containerid), headers=headers)

    return r.status_code


def restart_container(token, containerid):
    headers = {'Content-type': 'application/json',
               'Authorization': 'Token {}'.format(token)}
    r = requests.put(ENV + '/api/v1/containers/{containerid}/actions/restart'.format(containerid=containerid),
                     headers=headers)

    return r.status_code


def save_container_to_images(token, containerid):
    headers = {'Content-type': 'application/json',
               'Authorization': 'Token {}'.format(token)}
    r = requests.post(ENV + '/api/v1/containers/{containerid}/tag'.format(containerid=containerid),
                      headers=headers)

    result_json = json.loads(r.text)
    return result_json


def get_containers_list(token):
    headers = {'Content-type': 'application/json',
               'Authorization': 'Token {}'.format(token)}
    r = requests.get(ENV + '/api/v1/containers', headers=headers)
    result_json = json.loads(r.text)
    return result_json


@click.group()
def main(**kwargs):
    # print("This method has these arguments: " + str(kwargs))
    pass


@main.command("container-image-list")
@click.option('--app_key', default="07ed767760f74d8a868071144d1048e8", help='app_key')
@click.option('--app_secret', default="d965faa27f794e588c412ad90b6340fc", help='app_secret')
def do_container_image_list(app_key, app_secret):
    token = get_token(app_key, app_secret)
    image_result_json = get_container_images(token)

    headers = ["id", "name", "tag"]
    json_key_list = ["custom_images", "public_images"]
    headers, tabulate_data_list = multi_column_json_tabulate(image_result_json, json_key_list, headers)
    tabulate_print_info(headers, tabulate_data_list)


@main.command("container-show")
@click.option('--app_key', default="07ed767760f74d8a868071144d1048e8", help='app_key')
@click.option('--app_secret', default="d965faa27f794e588c412ad90b6340fc", help='app_secret')
@click.argument('containerid')
def do_container_show(app_key, app_secret, containerid):
    token = get_token(app_key, app_secret)
    container_result_json = get_container_info(token, containerid)

    json_key_list = ["id", "name", "status", "bandwidth", "public_ip", "image_id"]
    headers, tabulate_data_list = two_columns_json_tabulate(container_result_json, json_key_list)
    tabulate_print_info(headers, tabulate_data_list)


@main.command("container-flow")
@click.option('--app_key', default="07ed767760f74d8a868071144d1048e8", help='app_key')
@click.option('--app_secret', default="d965faa27f794e588c412ad90b6340fc", help='app_secret')
@click.argument('containerid')
def do_get_container_flow(app_key, app_secret, containerid):
    token = get_token(app_key, app_secret)
    container_result_json = get_container_flow(token, containerid)

    json_key_list = ["container_up_flow", "container_down_flow"]
    headers, tabulate_data_list = two_columns_json_tabulate(container_result_json, json_key_list)
    tabulate_print_info(headers, tabulate_data_list)


@main.command("container-to-image")
@click.option('--app_key', default="07ed767760f74d8a868071144d1048e8", help='app_key')
@click.option('--app_secret', default="d965faa27f794e588c412ad90b6340fc", help='app_secret')
@click.argument('containerid')
def do_save_container_to_images(app_key, app_secret, containerid):
    token = get_token(app_key, app_secret)
    container_result_json = save_container_to_images(token, containerid)

    json_key_list = ["repo_name", "tag"]
    headers, tabulate_data_list = two_columns_json_tabulate(container_result_json, json_key_list)
    tabulate_print_info(headers, tabulate_data_list)


@main.command("container-delete")
@click.option('--app_key', default="07ed767760f74d8a868071144d1048e8", help='app_key')
@click.option('--app_secret', default="d965faa27f794e588c412ad90b6340fc", help='app_secret')
@click.argument('containerid')
def do_delete_container(app_key, app_secret, containerid):
    token = get_token(app_key, app_secret)
    delete_container(token, containerid)


@main.command("container-restart")
@click.option('--app_key', default="07ed767760f74d8a868071144d1048e8", help='app_key')
@click.option('--app_secret', default="d965faa27f794e588c412ad90b6340fc", help='app_secret')
@click.argument('containerid')
def do_restart_container(app_key, app_secret, containerid):
    token = get_token(app_key, app_secret)
    restart_container(token, containerid)


@main.command("container-list")
@click.option('--app_key', default="07ed767760f74d8a868071144d1048e8", help='user tenantId')
@click.option('--app_secret', default="d965faa27f794e588c412ad90b6340fc", help='user tenantId')
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
    main()
