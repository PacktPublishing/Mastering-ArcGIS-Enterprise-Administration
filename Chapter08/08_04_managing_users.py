import collections
import time
import pandas as pd
from  arcgis.gis import GIS

gis = GIS("https://www.masteringageadmin.com/portal", "portaladmin", "somepass")
all_my_accounts = gis.users.search('!esri_')

l = []
for user in all_my_accounts:
    d = collections.OrderedDict()
    d['User Name'] = user.username
    d['First Name'] = user.firstName
    d['Last Name'] = user.lastName
    d['Email'] = user.email
    d['Role'] = user.role
    d['Provider'] = user.provider
    d['Level'] = user.level
    date_created = time.localtime(user.created/1000)
    d['Created'] = "{0}/{1}/{2}".format(date_created[1], date_created[2], date_created[0])
    l.append(d)
df = pd.DataFrame(l)
df