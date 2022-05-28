from contextlib import contextmanager
from sys import platform
import os


@contextmanager
def ip_information():
    try:
        if platform == "linux" or platform == "linux2":
            yield os.popen('ifconfig')
        elif platform == "win32":
            yield os.popen('ipconfig')
    finally:
        print("Ending...")


with ip_information() as info:
    print(info.read())