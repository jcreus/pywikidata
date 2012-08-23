# -*- coding: utf-8 -*-

import wikidata

#item = wikidata.Item({"cawiki":"Catalunya"}, {}, {}, {})
item = wikidata.api.getItemById(1)
print item.sitelinks

item.sitelinks["eswiki"] = "Barna"
item.sitelinks["cawiki"] = u"Sant Cugat del Vallès"

wikidata.api.save(item, 'A veure...')

print item.sitelinks
