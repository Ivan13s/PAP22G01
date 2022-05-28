import os
from contextlib import contextmanager
from sys import platform
import timeit


@contextmanager
def ip_information():
    try:
        if platform == "linux" or platform == "linux2":
            yield os.popen('ifconfig')
        elif platform == "win32":
            yield os.popen('ipconfig')

    finally:
        print('The end!')


result = timeit.timeit(f"""with ip_information() as info:
    info.read()""",
              setup=f"from {__name__} import ip_information",
              number=100)

print(result)