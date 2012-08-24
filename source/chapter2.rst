Items
*****
Items are a core part of pywikidata. They provide an abstraction to Wikidata items in the form of a class, Item(). Instead of dealing with JSON directly, it allows to change properties of the class.

Being a simple object (kind of a C struct), they can be easily Pickled to store them into files. Other parts of pywikidata will allow to work with them, and most functions use them.

Initializing an item
====================
To create a new item, the Item constructor can be used. It allows four parameters.

.. automodule:: wikidata

.. autoclass:: Item
    :members:

Obviously, however, one can create an empty Item and then set stuff via its properties.

Items have another property, *id*, which shouldn't generally be set manually. In case it's not defined when the item is saved, a new item will be created, and the item object will have the new id available at Item.id. When items are fetched by id, for example, the property is already defined.

Fetching items
==============
Pywikidata provides various ways to get an item. These are outlined below; you can see the full reference here at the last section of this manual.

.. function:: wikidata.api.getItemById(id)
.. function:: wikidata.api.getItemsById(ids)

   It returns either an item or a collection of items.

::

   import wikidata

   item = wikidata.api.getItemById(1)
   items = wikidata.api.getItemsById([4,8,15,16,23,42])

You can also select by interwikis.

.. function:: wikidata.api.getItemByInterwiki(site, title)
.. function:: wikidata.api.getItemsByInterwiki(sites, titles))
.. function:: wikidata.api.getItemsByInterwiki(sitesandtitles)

   It blah blah blah

::

   import wikidata

   item = wikidata.api.getItemByInterwiki("cawiki","Catalunya")
   items = wikidata.api.getItemsById(["cawiki","enwiki"],["Catalunya","Barcelona"])
   items = wikidata.api.getItemsById([["cawiki","Catalunya"], ["enwiki","Barcelona"]]) # Equivalent to above

Modifying items
===============
Now items can be modified. For example:

::

   import wikidata

   item = wikidata.api.getItemByInterwiki("cawiki","Catalunya")
   item.sitelinks["enwiki"] = "Catalonia"

Saving items
============
Items can be saved via ``wikidata.api.save``.

.. function:: wikidata.api.save(item, summary="")
.. function:: wikidata.api.save(items, summary="")

::

   import wikidata

   item = wikidata.api.getItemByInterwiki("cawiki","Catalunya")
   item.sitelinks["enwiki"] = "Catalonia"
   wikidata.api.save(item, "Edit summary")

::

   import wikidata

   item = wikidata.Item()
   wikidata.api.save(item, "Edit summary")
   # Now item.id contains the assigned id. Redirects in sitelinks will be also here resolved.
