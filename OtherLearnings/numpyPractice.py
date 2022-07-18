from numpy import *
from main import printIfItisMain

print("numpyPractice says" + __name__)

#decorators

# def customdivision(a,b):
#     print(a/b)
#
# def smart_customdivision(func):
#     def innerdivision(a,b):
#         if a<b:
#             a,b = b,a
#         return func
#     return innerdivision
#
#
# customdivision = smart_customdivision(customdivision(2,4))
#customdivision(2,4)


# from functools import reduce
#
# lst = [21,12,23,55,7,20]
# even = list(filter(lambda a:a%2==0,lst))
#
# result = reduce(lambda a,b:a+b,even)
# print(result)

#lambda expressions
# multiplication = lambda a,b:a*b
#
# result = multiplication(10,2)
# print(result)

#factorial

# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#             fact=fact*i
#             print(fact)
#
#     return fact
#
# ans=factorial(5)
#
# print("Answer is ",ans)

#fibonacci numbers

#0,1,1,2,3,5,8,13..

# def feb(n):
#     a=0
#     b=1
#
#     print(a)
#     print(b)
#
#     for i in range(2,n):
#         c = a+b
#         a=b
#         b=c
#         print(c)
#
# feb(5)
#

#count even and odd numbers.

# lst = [23,33,44,46,2,8]
# def count(lst):
#     even=0
#     odd=0
#
#     for i in lst:
#         if i%2==0:
#             even+=1
#         else:
#             odd+=1
#
#     return even,odd
#
# even,odd = count(lst)
# print("Even count {} and Odd count {}".format(even,odd))

#Global and globals()
# a=100
#
# def something():
#     a=200
#     #global a
#     globals()['a']=300
#     print("in function value :",a)
#
#
# something()
# print("out value :",a)

# def person(name,**b):
#     print(name)
#     for i,j in b.items():
#         print(i,j)
#
#
# person("sanjay",age=39,city='vadodara',mobile=983242)

# def add(a,b):
#     return a+b
#
# c = add(array([1,2,3,4]),array([5,6,7,8]))
# print(c)

# arr1 = array([
#                 [2,3,4],
#                 [5,6,7],
#                 [1,2,3]
#             ])
#
# #arr2 = arr1.flatten()
# m = matrix(arr1)
#
# print(m)
# print (diagonal(m))