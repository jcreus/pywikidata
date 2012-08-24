Advanced: custom API and Config instances
*****************************************
``wikidata.api`` and ``wikidata.config`` are, really, instances of ``api.API`` and ``configReader.Config``. ``wikidata.py`` creates variables config (Config using config.py as a file) and api (Api using config as configuration). However, one can create another API object and give it other configuration, operating separately.
