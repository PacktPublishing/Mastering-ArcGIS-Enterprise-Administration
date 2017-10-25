import arcpy
ds = "Database Connections\owner@SDEPROD@localhost.sde\SDEPROD.OWNER.USGS_StreamGauges"
arcpy.ChangePrivileges_management(ds, “webreader”, “GRANT”, “GRANT”)
