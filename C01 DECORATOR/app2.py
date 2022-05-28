#execute only during working hours (9-17)
    # - working hours prints message
    # -outside of working hours functions does not execute
import time


import time
from functools import wraps
import datetime


def working_hours(start, stop):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if time.localtime().tm_hour not in range(start.hour, stop.hour):
                return
            result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


@working_hours(datetime.time(hour=9), datetime.time(hour=22))
def alarm():
    print("Wack up")


alarm()