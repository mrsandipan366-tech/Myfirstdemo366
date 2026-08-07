class car:
    count=0
    def __init__(self, number):
        self.number=number
        car.count+=1
    def january(self):
        return self.number

class electriccar(car):
    def january(self):
        return self.number

class petrolcar:
    pass


a=car(500)
print(a.january())
b=electriccar(699)
print(b.january())

print(b.count)