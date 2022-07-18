class PrintUsingYield:

    def show(self):
        for i in range(5):
            yield i

obj = PrintUsingYield()
values = obj.show()
#print(values.__next__())

for i in values:
    print(next(values))