# Basic decorators
def area(length=10, width=5):
    """ Calculates Area or ractangle"""
    return length * width

# print(area())
#
# print(50 * '#')
#
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print(f'Calculating result for: {func.__name__}')
#         result = func(*args,**kwargs)
#         print(f"Result is: {result}")
#         print('Completed Execution')
#         return result
#     return wrapper
# print(area(length=5,width=5))
# area=decorator(area)
# print(area(length=5,width=3))
# # result = decorator(func=area)
# # print(result())
# # print(type(result))
#
#
# #delay for debuging
# import time
#
# def delay_with_args(delay_time=10):
#     def delay(func):
#         def wrapper(*args, **kwargs):
#             time.sleep(delay_time)
#             result = func(*args,**kwargs)
#             return result
#         return wrapper
#     return delay
# print(area(length=5,width=5))
# area=delay_with_args(delay_time=10)(area())
# print(area(lenth=5,width=5))
#


#Identity of function
from functools import wraps
def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args,**kwargs)
        return result +1
    return wrapper

print(area.__doc__)
print(decorator(area).__doc__)
print(decorator(area).__doc__)
print(decorator(area).__name__)















