ws = r'Database Connections\owner@SDEPROD@localhost.sde'

indexes = [{"fc": "wHydrant", 
            "index_name": "IDX_HYD_FID", 
            "field": "FID"},
           {"fc": "wHydrant", 
            "index_name": "IDX_HYD_STR_STN", 
            "field": ["STREETNO", "STREETNAME"]}]

desc = arcpy.Describe(os.path.join(ws, index.get("fc")))
for index in indexes:
    for g in desc.indexes:
        if g.name == index.get("index_name"):
            arcpy.RemoveIndex_management(os.path.join(cws, index.get("fc")), 
                                         index.get("index_name"))
    arcpy.AddIndex_management(os.path.join(cws, index.get("fc")), 
                              fields, index.get("field"))
        