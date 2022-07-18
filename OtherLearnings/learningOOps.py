class car:

    def __init__(self,model,year,brand):
        self.model = model
        self.year = year
        self.brand = brand

    def car_details(self):
        print(self.model)
        print(self.year)
        print(self.brand)
    pass

mahindra = car("LX",2022,"Mahindra")
mahindra.car_details()