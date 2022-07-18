class student:

    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

    def show(self):
        print(self.name,self.rollno)


s1 = student('sanjay',33)
s2 = student('shaurya',3)

s1.show()
s2.show()