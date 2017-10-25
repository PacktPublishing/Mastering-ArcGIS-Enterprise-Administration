import arcpy
import os

src_gdb = r"Database Connections\owner@sandbox@MSS2014.sde"
tgt_gdb = r"C:\Projects\Chad\Writing\mastering-arcgis-ent-admin\content\data\06_02_load_data.gdb"

layer_list = []
with open("06_02_layer_inputs.txt", "rb") as f:
    for line in f:
        layer_list.append(line.strip())

for layer in layer_list:
    print "Deleting old features from '{0}' in target...".format(layer)
    arcpy.DeleteFeatures_management(
        os.path.join(tgt_gdb, layer)
    )
    print "Appending new features from source into '{0}' in target geodb...".format(layer)
    arcpy.Append_management(
        os.path.join(src_gdb, layer),
        os.path.join(tgt_gdb, layer),
        "NO_TEST", "", ""
    )
