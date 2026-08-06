class car:
    total_car=0
    def __init__(self, brand, model):
        self.brand=brand
        self.model=model
        car.total_car+=1

    def get_brand(self):
        return self.brand + "1"


    def fueltype(self):
        return "petrol"

    def full_name(self):
        return f"{self.brand}{self.model}"


    @staticmethod
    def general_discription():
             return "car is a means of transport"


class electriccar(car):
    def __init__(self, brand , model, batterysize):
        super().__init__(brand, model)
        self.batterysize=batterysize

    def fueltype(self):
            return "eletric charge"


    


mytesla=electriccar("tesla","suiiiiii","86kw")

print(mytesla.brand)
print(mytesla.fueltype())

mytata=car("tata", "suffery")
print(mytata.fueltype())

print(car.total_car)




MY_car=car("toyota","corola")
print(MY_car.model)
print(MY_car.full_name())

print(MY_car.general_discription())

# mycar=car("tata", "nano")
# print(mycar.model)



