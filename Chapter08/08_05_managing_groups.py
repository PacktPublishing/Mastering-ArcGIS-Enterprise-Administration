from  arcgis.gis import GIS
gis = GIS("https://www.masteringageadmin.com/portal", 
          "portaladmin", "somepass”)

groups = gis.groups.search('owner:portaladmin')

for group in groups:
    print(group.title)
    mems = group.get_members()
    print("\tOwner: {0}".format(mems['owner']))
    print("\tAdmins: {0}".format(", ".join(mems['admins'])))
    print("\tUsers: {0}".format(", ".join(mems['users'])))
