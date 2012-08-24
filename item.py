# -*- coding: utf-8 -*-

class Item:

    def __init__(self, sitelinks={}, aliases={}, labels={}, descriptions={}):
        self.id = None
        self.sitelinks = sitelinks
        self.aliases = aliases
        self.labels = labels
        self.descriptions = descriptions
