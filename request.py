# -*- coding: utf-8 -*-

import urllib2
from urllib import urlencode
import json
import cookielib

import errors

class RequestHandler:

    def __init__(self, config):
        self.config = config
        self._cj = cookielib.CookieJar()
        self._opener = urllib2.build_opener(
                urllib2.HTTPCookieProcessor(self._cj)
        )
        self._editToken = None
        if config["username"] and config["password"]:
            self.login(config["username"], config["password"])
    
    def login(self, user, password):
        """Logins with arguments user and password."""
        def log(self, user, passwd, token=None):
            data = {'action': 'login', 'lgname': user, 'lgpassword': passwd}
            if token:
                data['lgtoken'] = token
            result = self.post(data)
            if result['login']['result'] == 'Success':
                # Ok, we've logged in. Now get an edit token (only needed one time).
                self._editToken = self.getToken()
                return True
            elif result['login']['result'] == 'NeedToken' and not token:
                return log(self, user, passwd, result['login']['token'])
            else:
                return False

        return log(self, user, password)

    def get(self, params):
        """Issues a GET API request and returns a dictionary, or raises an error if appropiate."""
        params["format"] = "json"
        a = urllib2.Request(self.config["api"]+"?"+self.encode(params))
        content = urllib2.urlopen(a).read()
        js = json.loads(content)
        self._checkErrors(js)
        return js

    def post(self, params):
        """Issues a POST API request and returns a dictionary, or raises an error if appropiate."""
        params["format"] = "json"
        a = urllib2.Request(self.config["api"], self.encode(params))
        content = self._opener.open(a).read()
        js = json.loads(content)
        self._checkErrors(js)
        return js

    def encode(self, params):
        p2 = {}
        for param in params:
            p2[param] = unicode(params[param]).encode('utf-8')
        return urlencode(p2)

    def postWithToken(self, params):
        """Issues a POST API request (requesting a token beforehand) and returns a dictionary, or raises an error if appropiate."""
        params["token"] = self._editToken
        return self.post(params)

    def getToken(self):
        """Returns a token."""
        return self.post({"action": "tokens", "format": "json", "type": "edit"})["tokens"]["edittoken"]

    def _checkErrors(self, data):
        if not "error" in data:
            return
        code = data["error"]["code"]
        error = None
        if code == "cant-edit":
            error = errors.PermissionError
        elif code == "no-such-item-id":
            error = errors.ItemNotFoundError
        else:
            error = errors.UnknownError
        raise error(data["error"]["info"])
