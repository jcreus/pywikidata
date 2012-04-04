# -*- coding: utf-8 -*-

"""
Python interface to the Wikidata API.

The API hasn't been developed yet, so this is just the infrastructure.
"""

"""
Private class. Use the config object instead, which is an instance of this class.
"""
class _Config:
    config = {}
    def __init__(self, uri):
        self.configFile = uri
        try:
            execfile(self.configFile, {}, self.config)
        except IOError:
            pass
    def __getitem__(self, name):
        return self.config.get(name, None)

    def __setitem__(self, name, value):
        self.config[name] = value
        self._save()

    def _save(self):
        configStr = ""
        for i in self.config:
            configStr += i+" = "+repr(self.config[i])+"\n"
        with open(self.configFile, 'w') as f:
            f.write(configStr)

BADGE_NONE = 0
BADGE_FA = 1
BADGE_GA = 2

""" Internal API class. Use api object instead. """
class _API:
    def __init__(self):
        pass

    def getData(self, iID, language=None):
        pass

    def getItemForArticle(self, language, title): # the spec says getIdByWikipedia, I think this way is more clear
        pass

    def getDataForArticle(self, language, title, dataLang=None):
        return self.getData(self.getItemForArticle(language, title), dataLang)

    def setLanguageLink(self, iID, language, title, badge=None):
        pass

    def linkWikipedias(self, language_from, title_from, language_to, title_to, badge_to=None):
        self.setLanguageLink(self.getItemForArticle(language_from, title_from), language_to, title_to, badge_to)

    def setLabel(self, iID, language, label):
        pass

    def setDescription(self, iID, language, description):
        pass

    def addAlias(self, iID, language, alias):
        pass

    def removeAlias(self, iID, language, alias):
        pass

    def autocomplete(self, language, fragment, hints=None):
        pass

api = _API()
config = _Config('config.py')
