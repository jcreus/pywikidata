# -*- coding: utf-8 -*-

import wikidata

"""
Create items
~~~~~~~~~~~~
"""
item = wikidata.Item({"cawiki":"Catalunya"}, {}, {}, {})
#                     sitelinks, aliases, labels, descriptions
item2 = wikidata.Item({"cawiki":"Catalunya"}, {}, {}, {})

wikidata.api.save([item, item2], 'Edit summary')

"""
Get an item by id
~~~~~~~~~~~~~~~~~
"""
item = wikidata.api.getItemById(1) # getItemsById also works

"""
Modify an item
~~~~~~~~~~~~~~
"""
item.sitelinks["cawiki"] = u"Sant Cugat del Vallès"
item.sitelinks["eswiki"] = "Barna"

wikidata.api.save(item, 'Edit summary')

"""
Other notes
~~~~~~~~~~~

The locally stored item is updated with the changes remotely, e.g. if Wikidata has resolved a redirection.
"""
print item.sitelinks # eswiki points to Barcelona, following the redirect
