import pandas as pd
from  arcgis.gis import GIS
gis = GIS("https://www.masteringageadmin.com/portal", 
          "portaladmin", “password”)

xls_file = pd.ExcelFile(r"C:\data\station-data.xlsx")
df = xls_file.parse('Sheet1')

df.to_csv(r"C:\data\station-data.csv")
csv_item = gis.content.add(item_properties={'title':'mt kessler'}, 
                           data=r"C:\data\station-data.csv")
stations_item = csv_item.publish()

map1 = gis.map("Fayetteville, AR")
map1

map1.add_layer(stations_item)
stations_item.url