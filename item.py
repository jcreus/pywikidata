# -*- coding: utf-8 -*-

class Item:
    def __init__(self, sitelinks=None, aliases=None, labels=None, descriptions=None):
        self.id = None
        self.sitelinks = sitelinks
        self.aliases = aliases
        self.labels = labels
        self.descriptions = descriptions
