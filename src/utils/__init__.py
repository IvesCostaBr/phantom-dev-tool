import logging
from colorama import Fore
import os


ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def show_log(message: str):
    print(Fore.BLUE + message)
