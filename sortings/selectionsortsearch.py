def sort(list):

    for i in range(len(list)):
        minpos=i
        for j in range(i,len(list)):
            if list[j]<list[minpos]:
                minpos=j

        temp = list[i]
        list[i]=list[minpos]
        list[minpos]=temp



list = [32,33,1,1,3,5]

sort(list)
print(list)