#!/usr/bin/env python
# encoding: utf-8

import json

import requests
from tabulate import tabulate
import click


def multi_column_json_tabulate(json, json_key_list, headers_list):
    # second_key_list is headers
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
    tabulate_data_list = []

    for key in json_key_list:
        try:
            result_list = {key: json[key]}
            tabulate_data_list.append([key, result_list[key]])
        except:
            pass


    headers = ["Field", "Value"]
    return headers, tabulate_data_list