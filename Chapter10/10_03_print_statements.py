import arcpy

result = arcpy.GetCount_management(
    r"C:\Projects\GDBs\Sandbox.gdb\StudyAreas"
)
record_count = int(result.getOutput(0))
if record_count > 0:
    arcpy.FeatureClassToFeatureClass_conversion(
        r"C:\Projects\GDBs\Sandbox.gdb\StudyAreas",
        r"C:\Projects\GDBs\Sandbox.gdb",
        "ActiveStudyAreas"
    )
