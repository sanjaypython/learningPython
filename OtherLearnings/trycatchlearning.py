
a=4
b=0

try:
    c=a/b
    print(c)
except ZeroDivisionError:
    print("ZeroDivisionError")
finally:
    print("caught exception")
