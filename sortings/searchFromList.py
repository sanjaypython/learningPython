
#finding index at which given number is present in list
pos=0
list = [22,1,2,3,4,5,6,8]
n=5


def search(list, n):

    for i in list:
        if i == n:
            globals()['pos']=i
            return True
    else:
        return False




if search(list,n):
    print("Found at " , pos)
else:
    print("Not found")