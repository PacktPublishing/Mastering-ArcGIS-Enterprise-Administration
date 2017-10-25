import arcpy
ws = r'Database Connections\sde@SDEPROD@localhost.sde'
users = arcpy.ListUsers(ws)
for user in users:
    print "{0}: {1}".format(user.ID, user.Name)
