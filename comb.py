#!/usr/bin/env python
# encoding: utf-8

from containers import *
from repositories import *
from apps import *


click = click.CommandCollection(sources=[container, apps, repositories])

if __name__ == '__main__':
    click()