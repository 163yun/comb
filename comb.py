#!/usr/bin/env python
# encoding: utf-8

import json

import requests
from tabulate import tabulate

from containers import *
from repositories import *
from apps import *
from secret_keys import *

from json_tabulate import *
import click

# user token
HEADERS = {'Content-type': 'application/json'}
ENV = 'https://open.c.163.com'

ACCESS_KEY = '07ed767760f74d8a868071144d1048e8'
ACCESS_SECRET = 'd965faa27f794e588c412ad90b6340fc'



if __name__ == '__main__':
    do_container_list(ACCESS_KEY, ACCESS_SECRET)
    # do_repositories_list(ACCESS_KEY, ACCESS_SECRET)
    do_container_show(ACCESS_KEY, ACCESS_SECRET, "347339")