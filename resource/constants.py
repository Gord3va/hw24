import os.path
from typing import List

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "../data")
COMMANDS: List[str] = ['filter', 'map', 'post', 'sort', 'unique', 'limit', 'regex']
