from from_root import from_root
from ner.constants import ARTIFACTS_KEY, LOGS_KEY
import logging
import os


# logs_path = os.path.join(from_root(), ARTIFACTS_KEY, LOGS_KEY, LOGS_KEY)
logs_path = os.path.join(ARTIFACTS_KEY, LOGS_KEY, LOGS_KEY)

print(from_root())
logging.basicConfig(filename=f"{logs_path}.txt",
                    format='[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)

