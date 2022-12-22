import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

TARGETS_FILENAME = os.getenv("TARGETS_FILENAME") or "targets.csv"
TARGETS_FILE_PATH = os.path.join(dirname, "..", TARGETS_FILENAME)
