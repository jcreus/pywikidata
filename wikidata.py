# -*- coding: utf-8 -*-

"""
Python interface to the Wikidata API.
"""

from item import Item # So that wikidata.Item can be used.

from configReader import _Config
from api import _API

import errors

config = _Config('config.py')
if not config["api"]:
    raise errors.ConfigurationError("An API url needs to be defined in config.py")

api = _API(config)
