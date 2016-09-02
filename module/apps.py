import click
from tabulate import tabulate

from lib.token import *
from lib.json_tabulate import *


def get_app_images(token):
    headers = {'Content-type': 'application/json',
               'Authorization': 'Token {}'.format(token)}
    r = requests.get(COMB_OPENAPI + '/api/v1/apps/images', headers=headers)
    result_json = json.loads(r.text)
    return result_json


@click.group()
def apps(**kwargs):
    # print("This method has these arguments: " + str(kwargs))
    pass


@apps.command("app-image-list")
@click.option('--app_key', default=ACCESS_KEY, help='app_key')
@click.option('--app_secret', default=ACCESS_SECRET, help='app_secret')
def do_app_image_list(app_key, app_secret):
    token = get_token(app_key, app_secret)
    image_list_result_json = get_app_images(token)

    headers = ["id", "name", "tag", "weight", ]
    json_key_list = ["custom_images", "public_images"]
    headers, tabulate_data_list = multi_column_json_tabulate(image_list_result_json, json_key_list, headers)
    tabulate_print_info(headers, tabulate_data_list)


def tabulate_print_info(headers, result_metadata_list):
    print tabulate(result_metadata_list, headers, tablefmt="psql", stralign="left", numalign="left")


if __name__ == '__main__':
    apps()



