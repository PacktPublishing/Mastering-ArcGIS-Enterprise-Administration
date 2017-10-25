import arcpy
ws = r'Database Connections\sde@SDEPROD@localhost.sde'
users = arcpy.ListUsers(ws)
for user in users:
	arcpy.DisconnectUser(ws, user.ID)
