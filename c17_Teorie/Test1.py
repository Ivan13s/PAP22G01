from functools import wraps


# def decorator1(func):
#     @wraps(func)
#     def wrapper(*args,**kwargs):
#         return tuple(func(*args,**kwargs))
#     return wrapper
#
# def decorator2(obj_type):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args,**kwargs):
#             return obj_type(func(*args,**kwargs))
#         return wrapper
#     return decorator
#
#
# @decorator1
# @decorator2(str)
# def my_func():
#     print('some_value')






# exercitiul 2
# def decorator(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         return int(func(*args, **kwargs))
#
#     return wrapper


#exercitiul 3
# class MyClass:
#
#     @staticmethod
#     def my_func(self, message):
#         print(message)
#
#
# MyClass.my_func("some_text")

#exercitiul 4

# def decorator(func):
#     def wrapper():
#         return func()
#     return wrapper
#
# @decorator
# def test(message):
#     print(message)
#
# test()

#exercitiul 5

# def decorator(func):
#     def wrapper(*args,**kwargs):
#         result=func(*args,kwargs)
#         return result +1
#     return wrapper
#
# @decorator
# def test():
#     print('test')
#
# print(test.__name__)


