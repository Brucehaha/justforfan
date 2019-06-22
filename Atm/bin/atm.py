import os
import sys

#
# print(os.path.abspath(__file__)) #absolute path
#
# print(__file__)# relative path

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(BASE_DIR)

sys.path.append(BASE_DIR)
from core import main
from conf import settings

main.login() 