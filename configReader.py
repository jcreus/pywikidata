# -*- coding: utf-8 -*-

class _Config:
    """Internal, reads configuration from a file. Use the config object instead."""

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
