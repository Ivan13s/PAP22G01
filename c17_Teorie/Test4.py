# class MyContext:
#
#     def __enter__(self):
#         print('enter')
#
#     def __exit__(self,exc_type,exc_val,exc_tb):
#             print('exit')
#

#exercitiul 2
# import timeit
#
# print(type(timeit.timeit(lambda:"-".join(map(str,range(100))),number=1000)))

#exercitiul 3
# from contextlib import contextmanager
#
#
# @contextmanager
# def test(value):
#     try:
#         yield value.pop()
#     except Exception:
#         yield True
#     finally:
#         pass
# with test("test") as t:
#     print(t)

#exercitiul 4
# import matplotlib.pyplot as plt
# fig1,(a,b)=plt.subplots(nrows=1,ncols=2,sharex='all')
# a.plot([i for i in range(10)])
# b.plot([1 for i in range(10)])
# plt.show()

#exercitiul 5
# import timeit
#
#
# def test():
#     print('testing...')
#     for _ in range(10):
#         timeit.timeit(f"test()"),
#         setup=f('from __main__ import test',number=100)
#
