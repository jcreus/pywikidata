# -*- coding: utf-8 -*-

""" Subclassed dictionaries, to keep track of the changed properties. """

class BaseCollection(dict):

	def __init__(self, *args, **kwargs):
		self.changed = {}
		super(BaseCollection, self).__init__(*args, **kwargs)

	def __setitem__(self, key, value):
		self.changed[key] = value
		super(BaseCollection, self).__setitem__(key, value)


	def __delitem__(self, key):
		self.changed[key] = ""
		super(BaseCollection, self).__delitem__(key)

	def export(self):
		# Basically, a list of dictionaries

		ret = []
		for key in self.changed:
			ret.append({self.val1:key, self.val2:self.changed[key]})

		return ret

class SitelinkCollection(BaseCollection):
	val1 = "site"
	val2 = "title"

class AliasCollection(BaseCollection):
	val1 = "language"
	val2 = "value"

class LabelCollection(BaseCollection):
	val1 = "language"
	val2 = "value"

class DescriptionCollection(BaseCollection):
	val1 = "language"
	val2 = "value"