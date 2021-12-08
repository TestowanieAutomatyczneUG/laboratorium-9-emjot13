from lab9.zad2.src.car import Car


class CarImpl:
    def __init__(self, car: Car):
        self.car = car

    
    def needsFuel(self):
        if self.car.needsFuel():
            return "car needs more fuel"
        return "car doesn't need any fuel"
    

    def getEngineTemperature(self):
        if self.car.getEngineTemperature():
            temperature = self.car.getEngineTemperature()
            return f"The engine's temperature is {temperature} °C"
        return "Can't get the engine's temperature"
    
    def driveTo(self, destination):
        if self.car.driveTo(destination):
            return f"Current destination is {destination}"
        return f"The destination hasn't been set"


car = Car()
obj = CarImpl(car)
print(obj.driveTo("lol"))
