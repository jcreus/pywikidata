# -*- coding: utf-8 -*-

from propertycollections import *

class Item:

    def __init__(self, sitelinks={}, aliases={}, labels={}, descriptions={}):
        self.id = None
        self.sitelinks = SitelinkCollection(sitelinks)
        self.aliases = AliasCollection(aliases)
        self.labels = LabelCollection(labels)
        self.descriptions = DescriptionCollection(descriptions)