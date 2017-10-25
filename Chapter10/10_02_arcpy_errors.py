import arcpy
import daiquiri
import datetime
import inspect
import logging
import os
import sys
import traceback
from daiquiri import formatter

def trace_error():
    """
    Returns line, filename and error from a traceback.
    :return: Line, filename and error from a traceback.
    """
    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]
    filename = inspect.getfile(inspect.currentframe())
    line = tbinfo.split(", ")[1]
    synerror = traceback.format_exc().splitlines()[-1]

    return line, filename, synerror

daiquiri.setup(
    outputs=(
        daiquiri.output.TimedRotatingFile(
            "python_logging.txt",
            formatter=daiquiri.formatter.ColorFormatter(
                fmt="%(asctime)s - %(filename)s - %(lineno)d - %(levelname)s - %(message)s"
            ),
            interval=datetime.timedelta(days=7),
            backup_count=10
        ),
        daiquiri.output.Stream(
            sys.stdout,
            formatter=daiquiri.formatter.ColorFormatter(
                fmt="%(asctime)s - %(filename)s - %(lineno)d - %(levelname)s - %(message)s"
            )
        ),
    ),
    level=logging.INFO)
logger = daiquiri.getLogger(__name__)

try:
    # Do something
    arcpy.GetCount_management("")
except arcpy.ExecuteError:
    line, filename, synerror = trace_error()
    logger.error("\n\n\tError on {0} of '{1}'.\n".format(line, filename))
    errs = arcpy.GetMessages(2)
    logger.error("arcpy errors: {0}".format(errs))
except:
    line, filename, synerror = trace_error()
    logger.error("\n\n\tError on {0} of '{1}'. Message: {2}\n".format(line, filename, synerror))
finally:
    logger.info("Finished processing.\n\n")