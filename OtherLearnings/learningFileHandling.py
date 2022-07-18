file1 = open("data.txt", 'r')

file2 = open("new.txt", 'a')

for i in file1:
    file2.write(i)
