#finding index at which given number is present in list
pos=0
list = [1,2,3,4,22]
n=22


def search(list, n):
    l=0
    u=len(list)-1

    for i in list:
        mid = (l+u)//2
        if n==list[mid]:
            globals()['pos']=i
            return True
        else:
            if list[mid]<n:
                l=mid+1
            else:
                u=mid-1
    else:
        return False




if search(list,n):
    print("Found at " , pos)
else:
    print("Not found")