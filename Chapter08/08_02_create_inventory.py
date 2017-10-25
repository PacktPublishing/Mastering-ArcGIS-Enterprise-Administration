import arcgis
import collections
from arcgis.gis import GIS
import pandas as pd
import pprint

gis = GIS("https://www.masteringageadmin.com/portal", "portaladmin", "somepass")
search_results = gis.content.search(query="tags:city-maps", item_type="Web Map")

l = []
for s in search_results:
    
    wmo = arcgis.mapping.WebMap(s)
    ops_layers = wmo['operationalLayers']
    basemap_layers = wmo['baseMap']['baseMapLayers']

    for op_layer in ops_layers:
        d = collections.OrderedDict()
        d["Web Map Name"] = s.title
        d["Web Map Item ID"] = s.itemid
        d["Layer Type"] = "Operational Layer ({0})".format(op_layer["layerType"])
        d["Layer URL"] = op_layer["url"]  
        l.append(d)
        
    for base_layer in basemap_layers:
        j = collections.OrderedDict()
        j["Web Map Name"] = s.title
        j["Web Map Item ID"] = s.itemid
        j["Layer Type"] = "Basemap Layer ({0})".format(base_layer["layerType"])
        j["Layer URL"] = base_layer["url"]  
        l.append(j)
        
df = pd.DataFrame(l)
writer = pd.ExcelWriter('output.xlsx')
df.to_excel(writer, sheet_name='Sheet1')
writer.save()