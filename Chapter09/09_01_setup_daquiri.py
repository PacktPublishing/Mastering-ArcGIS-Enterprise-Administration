import daiquiri
import datetime
import logging

daiquiri.setup(
    outputs=(
        daiquiri.output.TimedRotatingFile(
            config["logging"]["file"],
            formatter=daiquiri.formatter.TEXT_FORMATTER(
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

logger.info("Info message")
logger.warning("Warning message")
logger.error(“Oops, something went really wrong”)
