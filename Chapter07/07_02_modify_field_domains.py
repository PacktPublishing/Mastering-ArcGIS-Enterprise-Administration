import arcpy
import os

input_ds = r"C:\Projects\HCWA\ETL\GDBs\HCWA_LGIM.gdb\WaterDistribution"

field_domains = {"OWNEDBY": "hwAssetOwner",
                 "MAINTBY": "hwAssetManager"}

arcpy.env.workspace = input_ds

fcs = arcpy.ListFeatureClasses()
for fc in fcs:
    print fc
    fields = arcpy.ListFields(os.path.join(input_ds, fc))
    field_names = [field.name for field in fields]
    print field_names
    for k, v in field_domains.iteritems():
        if k in field_names:
            arcpy.AssignDomainToField_management(fc, k, v)