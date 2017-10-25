import arcgis
from arcgis.gis import GIS

gis = GIS("https://www.masteringageadmin.com/portal", "portaladmin", "pass")
search_results = gis.content.search(query="tags:city-maps", item_type="Web Map")
print(search_results)

for search_result in search_results:
    web_map = arcgis.mapping.WebMap(search_result)
    layers = web_map['operationalLayers']
    for layer in layers:
        print(layer['url'])

for search_result in search_results:
    web_map = arcgis.mapping.WebMap(search_result)
    layers = web_map['operationalLayers']
    for layer in layers:
        print(layer['url'])        
        new_url = (layer['url'].replace('http:', 'https:'))
        layer['url'] = new_url
        print(new_url)
    web_map['operationalLayers'] = layers
    web_map.update()

for search_result in search_results:
    web_map = arcgis.mapping.WebMap(search_result)
    layers = web_map['operationalLayers']
    for layer in layers:
        print(layer['url'])