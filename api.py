# -*- coding: utf-8 -*-

import json

from request import RequestHandler
from item import Item
import errors

from pprint import pprint

class API:

    def __init__(self, config):
        """Takes a configReader.Config object as an argument."""
        self.request = RequestHandler(config)
        self.config = config

    def getItemsById(self, ids=[]):
        """Returns an item collection. Takes a list of ids as an argument."""
        ids = [str(x) for x in ids]
        resp = self.request.get({"action":"wbgetentities", "ids": "|".join(ids)})
        items = self._createItemCollection(resp["entities"])
        return items

    def getItemById(self, iid):
        """Returns the item defined by the argument."""
        return self.getItemsById([iid])[0]

    def getItemsByInterwiki(self, arg1=[], arg2=[]):
        """Returns an item collection, coming from either a list of sites as the first argument and a list of titles as the second argument, or a list of tuples (site, title) as the only argument."""
        if arg1 and not arg2: # then arg1 is [[site,title],[site,title]]
            sites = [x[0] for x in arg1]
            titles = [x[1] for x in arg1]
        else:
            sites = arg1
            titles = arg2
        resp = self.request.get({"action":"wbgetentities", "sites": "|".join(sites), "titles": "|".join(titles)})
        items = self._createItemCollection(resp["entities"])
        return items

    def getItemByInterwiki(self, site, title):
        """Returns an item which has the requested site and title."""
        return self.getItemsByInterwiki([site], [title])[0]

    def save(self, items, comment=None):
        """Saves a list of items or a single item, with an optional second parameter being the summary."""
        if type(items) != list:
            items = [items]
        for item in items:
            params = {"action":"wbsetitem"}
            if item.id:
                params["id"] = item.id
            if comment:
                params["summary"] = comment
            if self.config["botflag"]:
                params["bot"] = "1"
            data = { "sitelinks": item.sitelinks.export(),
                     "aliases": item.aliases.export(),
                     "labels": item.labels.export(),
                     "descriptions": item.descriptions.export()
                   }

            params["data"] = json.dumps(data, ensure_ascii=False)
            self.request.postWithToken(params)

    def _createItemCollection(self, data):
        items = []
        for item in data:
            i = self._createItem(data[item])
            items.append(i)
        return items

    def _createItem(self, item, target=None):
        if not "sitelinks" in item:
            item["sitelinks"] = {}
        if not "aliases" in item:
            item["aliases"] = {}
        if not "labels" in item:
            item["labels"] = {}
        if not "descriptions" in item:
            item["descriptions"] = {}

        sitelinks = {}
        for x in item["sitelinks"]:
            sitelinks[x] = item["sitelinks"][x]["title"]
        aliases = {}
        for x in item["aliases"]:
            aliases[x] = [y["value"] for y in item["aliases"][x]]
        labels = {}
        for x in item["labels"]:
            labels[x] = item["labels"][x]["value"]
        descriptions = {}
        for x in item["descriptions"]:
            descriptions[x] = item["descriptions"][x]["value"]
        if target:
            target.sitelinks = sitelinks
            target.aliases = aliases
            target.labels = labels
            target.descriptions = descriptions
            if target.id and target.id != item["id"]:
                raise errors.ItemIDMismatch("Local item id does not match remote id. Have you added manually the id?")
            else:
                target.id = item["id"]
            return target
        else:
            i = Item(sitelinks, aliases, labels, descriptions)
            i.id = int(item["id"].replace("q",""))
            return i
