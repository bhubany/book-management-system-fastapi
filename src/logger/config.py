from datetime import datetime, timezone
import logging
from config.settings import Settings
import json

settings = Settings()


class JsonFormatter(logging.Formatter):
    def format(self, record):
        data = {
            'timestamp': datetime.fromtimestamp(timestamp=record.created, tz=timezone.utc).isoformat(),
            'context': record.levelname,
            'source': record.name,
            'message': record.getMessage()
        }
        return json.dumps(data)


def get_logger(name):
    logger = logging.getLogger(name)
    if not logger.hasHandlers():
        logger.setLevel(settings.log_level)
        handler = logging.StreamHandler()
        handler.setFormatter(JsonFormatter())
        logger.addHandler(handler)
    return logger
