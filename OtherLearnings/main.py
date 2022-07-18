import math,array

def printIfItisMain():
    if __name__ == "__main__":
        print("Hello")


printIfItisMain()
#from numpy import *

#adding two arrays using for loop

# arr0 = array.array('i',[12,13,14])
# arr1 = array.array('i',[2,3,5])
#
# dynamicarray = array.array('i',[])
#
# print(len(arr0))
# for i in range(len(arr0)):
#     temp = arr0[i]+arr1[i]
#     dynamicarray.append(temp)
#
#
# print(dynamicarray,end=" ")

# arr0 = zeros(5,int)
# arr1 = arr0.copy()
# arr0[1]=5
# print(id(arr0))
# print(id(arr1))
#
# arr0=arr0+5
# print(arr0+5)
#
# arr1=arr1+6
# print(arr1)
#
# print(min(arr0))
# print(max(arr1))

#
# #arr = array([12,12,12,4,5,6])
# arr = linspace(1,10,10)
# print(arr)
#
# arr = logspace(1,10,10)
# print(arr)

# numparray = array([12,15,5,4,3],int)
# print(len(numparray))

#
# dynamicarraycount = int(input("Specify the length of array"))
# dynamicarray = array.array('i',[])
#
# for i in range(dynamicarraycount):
#     vals = int(input("Enter next number"))
#     dynamicarray.append(vals)
#
# print(dynamicarray)

#search index of specified value in array
# searchvalue = int(input("Enter value to be searched : "))
# print(dynamicarray.index(searchvalue))


#array
# vals = array.array("i",[12,14,14,3,0])
# print(max(vals))
#
# print(sorted(vals))

#vals.reverse()
# print(vals[0])
#
# for i in range(len(vals)):
#     print(vals[i])


# newarray = array.array(vals.typecode,(a*a for a in vals))
# for i in newarray:
#     print(i)

#prime numbers
# num = 7
# print(math.sqrt(num))
# for i in range(2,num):
#     if num % i == 0:
#         print("number is not prime")
#         break
# else:
#     print("number is prime")


#For loop



# nums = [12,101,301,34]
# for num in nums:
#     if num % 5 == 0:
#         print(num)
#         break;
# else:
#         print("not found")

# for i in range(4):
#     for s in range(4-i):
#         print("# ",end="")
#     print("")


# for i in range(4,0,-1):
#     for s in range(i):
#         print("# ",end="")
#     print("")

# for i in range(1,21):
#     if i%3==0 or i%5==0:
#         continue
#     print(i)
#

# i=1;
# while i<=20:
#     if i%3!=0:
#         print(i)
#     i+=1

# for i in range(10,51,10):
#     print(i)

# listexample = [12,2.5,'sanjay']
#
# for i in listexample:
#     print(i)


# i=1
#
# while i<=5:
#     print("#",end="")
#     j = 1
#     while j<5:
#         print("#",end="")
#         j=j+1
#     i=i+1
#     print("")

#Given number is negative or positive
#
# #ifelse
# x=int(input("Enter number : "))
# if x<0:
#      print("It is a negative number")
# else:
#     print("It is positive number")

#     print("number is less than 0")
# else:
#     print("number is wrong")


#Take 3 numbers from user and find greatest of them
# first = int(input("Enter 1st number"))
# second = int(input("Enter 2nd number"))
# third = int(input("Enter 3rd number"))
#
# print("Maximum of number",max(first,second,third),)





#ifelse
# x=int(input("Enter number : "))
# if x==5:
#     print("Number is greater than 5")
# elif x<0:
#     print("number is less than 0")
# else:
#     print("number is wrong")

#evaluate expression by passing through console.
# result = eval(input("Enter expression to evaluate : "))
# print(result)


#taking user input
# a = int(input("Enter 1st number : "))
# b = int(input("Enter 2nd number : "))
# print(a+b)


# from math import sqrt
#
# print("hello world")
#
# num=5
# print(id(num))
#
#
#
# a=5
# b=6
# a,b=b,a
#
# print(a)
# print(b)
#
#
# import math
# x=sqrt(64)
# print(x)