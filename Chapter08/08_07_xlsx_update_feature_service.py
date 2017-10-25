import pandas as pd
from  arcgis.gis import GIS
from arcgis.features import FeatureLayerCollection

gis = GIS("https://www.masteringageadmin.com/portal", 
          "portaladmin", “password”)

flayer_item = gis.content.search('f017aa0e71y8d4e44be6cdb48f192aff3')
flayer_collection = FeatureLayerCollection.fromitem(flayer_item[0])

xls_file = pd.ExcelFile(r"C:\data\station-data.xlsx")
df = xls_file.parse('Sheet1')
df.to_csv(r"C:\data\station-data.csv")
flayer_collection.manager.overwrite(r"C:\data\station-data.csv")

map2 = gis.map("Fayetteville, AR")
map2

map2.add_layer(flayer_item)