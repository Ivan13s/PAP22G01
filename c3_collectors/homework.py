"""
Counted List
Create a class for an list like object based on UserList wrapper
https://docs.python.org/3/library/collections.html#collections.UserList
That object should have a method to return a Counter
https://docs.python.org/3/library/collections.html#collections.Counter
for all objects in the list
Counter should be updated automatically for at lest 2 methods (append, pop)
"""
from collections import UserList, Counter
# class Example(UserList)
#   ...
#
# x = Example(['1', '2', '3'])
# y = x.get_counter() # y contains Counter({'1':1, '2':1 '3':1})
# x.append(3)
# now y contains Counter({'1':1, '2':1 '3':2})

from collections import UserList, Counter

class LU(UserList):
    def __init__(self,lista=None):
        UserList.__init__(self,lista)
        self.data=[]
        if lista is not None:
            if isinstance(lista,type(self.data)):
                self.data[:]=lista
            elif isinstance(lista,UserList):
                self.data[:]=lista.data[:]
            else:
                self.data=list(lista)
    def counter(self):
        return Counter(self.data)
    def append(self,item):
        self.data.append(item)
    def pop(self,i:str=...):
        self.data.remove(i)
obiect = LU(['1', '2', '3'])
print(obiect.counter())
obiect.append('3')
print(obiect.counter())
obiect.pop('2')
print(obiect.counter())

