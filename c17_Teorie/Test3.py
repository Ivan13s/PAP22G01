from collections import deque, UserString, Counter


#class Test:
#     q=deque(maxlen=2)
#     def __add__(selfself, other, self=None):
#         self.q.append(other)
#         return self
#
# t=Test()
# x=t+1
# y=t+2
# z=t+3
# print(z.q.popleft())

#exercitiu 2
# d=deque([1,2,3,4]),maxlen=4)
# d.insert(0,5)
# print(list(d))

#exercitiu 3
# class MyStr(UserString):
#     def __add__(self,other):
#         result=[]
#         counter=0
#         for _ in self:
#             result.append(str(other[counter]))
#             counter+=1
#             return MyStr('').join(result)
#
# a=MyStr('text1')
# b=MyStr('text')
# print(b+a)

#exercitiul 4
# d=deque([1,2,3].maxlen=4)
# e=[4,5,6]
# d.extendleft(e)
# print(list(d))

#exercitiul 5
# class Test(Counter):
#     def __sub__(selfself, other, self=None):
#         for key,value in other.items():
#             self[key]-=value
#
# t1=Test('abbccc')
# t2=Test('abc')
# print(t1-t2)