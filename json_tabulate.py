#!/usr/bin/env python
# encoding: utf-8

import json

import requests
from tabulate import tabulate
import click


def multi_column_json_tabulate(json, json_key_list, headers_list):
    # handle column like this
    # +--------+------------+-------------+---------------+------------+
    # |     id | name       | status      | public_ip     |   image_id |
    # |--------+------------+-------------+---------------+------------|
    # | 630831 | testNagios | create_succ | 59.111.91.56  | 26413      |
    # | 628306 | test       | create_succ | 59.111.91.23  | 21697      |
    # | 193887 | myss2      | create_succ | 59.111.72.128 | 30656      |
    # +--------+------------+-------------+---------------+------------+


    # second_key_list define headers (e.g. ["id", "name", "status", "public_ip", "image_id"])
    # first key list is the list prepared to parse
    tabulate_data_list = []

    for key in json_key_list:
        for result in json[key]:
            try:
                result_list = {}
                this_result_list = []
                for header in headers_list:
                    result_list[header] = result[header]
                    this_result_list.append(result_list[header])
            except:
                pass

            tabulate_data_list.append(this_result_list)

    headers = headers_list
    return headers, tabulate_data_list


def two_columns_json_tabulate(json, json_key_list):
    # handle column like this
    # +---------------------+----------------------+
    # | Field               | Value                |
    # |---------------------+----------------------|
    # | id                  | 628306               |
    # | bandwidth           | 100                  |
    # | charge_type         | 1                    |
    # | created_at          | 2016-09-01T09:27:07Z |
    # | desc                |                      |
    # | env_var             | {}                   |
    # | image_id            | 21697                |
    # | name                | test                 |
    # | network_charge_type | 2                    |
    # | private_ip          | 10.173.32.61         |
    # | public_ip           | 59.111.91.23         |
    # | replicas            | 1                    |
    # | spec_id             | 1                    |
    # | ssh_key_ids         |                      |
    # | status              | create_succ          |
    # | updated_at          | 2016-09-01T09:27:40Z |
    # | use_public_network  | 1                    |
    # +---------------------+----------------------+

    tabulate_data_list = []

    for key in json_key_list:
        try:
            result_list = {key: json[key]}
            tabulate_data_list.append([key, result_list[key]])
        except:
            pass


    headers = ["Field", "Value"]
    return headers, tabulate_data_list