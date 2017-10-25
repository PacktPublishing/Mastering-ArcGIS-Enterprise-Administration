import arcgis
import json
import re
from arcgis.gis import GIS

codes = [11, 14, 30, 40]

gis = GIS("https://www.masteringageadmin.com/portal", "portaladmin", "somepass")
search_result = gis.content.search('title:LandUse-12', item_type = 'Web Map', outside_org = False)
#search_result[0]

web_map_object = arcgis.mapping.WebMap(search_result[0])

for code in codes:
    for layer in web_map_object['operationalLayers']:
        def_query = layer.get('layerDefinition')
        if def_query:
            query = def_query.get('definitionExpression')
            if query:
                print(query)
                search_obj = re.search(r"'[0-9]+'$", query)
                if search_obj:
                    if search_obj.group().replace("'", "").isdigit():
                        # Numeric county code
                        new_dq = query.replace(search_obj.group(), "'{0}'".format(code))
                        layer['layerDefinition']['definitionExpression'] = new_dq
                        dq = layer['layerDefinition'].get('definitionExpression')
                        print(dq)

    web_map_props = {"title": "LandUse-{0}".format(code),
                         "type": "Web Map",
                         "tags": "arcgis-api",
                         "text": json.dumps(web_map_object)}
    web_map_item = gis.content.add(web_map_props, folder="Replicating Content")
    web_map_item.share(everyone=True)