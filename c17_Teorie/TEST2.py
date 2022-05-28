# class A:
#     def __init__(self, value=3):
#         self.abc=value
#
#     def method1(self):
#         return self
#
#     def method2(self,value):
#         self._abc=value
#
#     abc=property(method1,method2)
#
#
# a=A()
# print(a.abc)
# import re
#
# text='Sample'
# pattern='(?P<text>.*)'
# print(re.search(pattern,text).group(0))

# class A:
#     def __init__(self,value=3):
#         self.abc=value
#
#     @property
#     def abc(self):
#         return self._abc
#     @abc.setter
#     def abc(self,value):
#         self._abc=5
#
# a=A()
# print(a.abc)