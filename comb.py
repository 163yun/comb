#!/usr/bin/env python
# encoding: utf-8

from module.containers import *
from module.repositories import *
from module.apps import *


click = click.CommandCollection(sources=[container, apps, repositories])

if __name__ == '__main__':
    click()