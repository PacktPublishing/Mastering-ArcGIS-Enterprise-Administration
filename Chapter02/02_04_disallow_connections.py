import arcpy
ws = r'Database Connections\sde@SDEPROD@localhost.sde'
arcpy.AcceptConnections(ws, False)
