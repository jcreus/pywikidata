# -*- coding: utf-8 -*-

from item import Item # So that wikidata.Item can be used.

from configReader import Config
from api import API

import errors

config = Config('config.py')
if not config["api"]:
    raise errors.ConfigurationError("An API url needs to be defined in config.py")

api = API(config)
