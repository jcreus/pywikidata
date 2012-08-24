The pywikidata manual
*********************
Pywikidata is a library which provides an interface to Wikidata's API.

Download it
===========
By now, the only way to download pywikidata is cloning the github repo.

    git clone https://github.com/jcreus/pywikidata.git

You might want to add it to the Python path so you can import it from all over the filesystem.


Simple configuration
====================
The file config.py includes some example settings, which have to be modified.

api
    This variable has to point to the URL of wikidata repo's API. For example, http://localhost/repo/api.php

username and password
    If present, they will be used to log in.

lang
    If present, queries will add a uselang parameter with the language code specified.
