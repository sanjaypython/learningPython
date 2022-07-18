#compare first 2 digits. if value at 1 index is greater than value at second index. Then swap.
#If value of 1st is smaller than 2nd , do not swap.


def sort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j] > list [j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp


list = [90, 0, 34, 23, 11, 76]
sort(list)
print(list)