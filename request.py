# -*- coding: utf-8 -*-

import urllib2
from urllib import urlencode
import json
import cookielib

class RequestHandler:
    def __init__(self, config):
        self.config = config
        self._cj = cookielib.CookieJar()
        self._opener = urllib2.build_opener(
                urllib2.HTTPCookieProcessor(self._cj)
        )
        if config["username"] and config["password"]:
            self.login(config["username"], config["password"])
    
    def login(self, user, password):
        def log(self, user, passwd, token=None):
            data = {'action': 'login', 'lgname': user, 'lgpassword': passwd}
            if token:
                data['lgtoken'] = token
            result = self.post(data)
            if result['login']['result'] == 'Success':
                return True
            elif result['login']['result'] == 'NeedToken' and not token:
                return log(self, user, passwd, result['login']['token'])
            else:
                return False

        return log(self, user, password)

    def get(self, params):
        params["format"] = "json"
        a = urllib2.Request(self.config["api"]+"?"+self.encode(params))
        content = urllib2.urlopen(a).read()
        return json.loads(content)

    def post(self, params):
        params["format"] = "json"
        a = urllib2.Request(self.config["api"], self.encode(params))
        content = self._opener.open(a).read()
        return json.loads(content)

    def encode(self, params):
        p2 = {}
        for param in params:
            p2[param] = unicode(params[param]).encode('utf-8')
        return urlencode(p2)

    def postWithToken(self, params):
        token = self.getToken(params["action"])
        params["token"] = token
        return self.post(params)

    def getToken(self, action):
        return self.post({"action": action, "format": "json", "gettoken": ""})[action]["itemtoken"]
