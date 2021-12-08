from unittest import TestCase
from unittest.mock import *
from lab9.zad2.src.car import Car
from lab9.zad2.src.CarImp import CarImpl


class Tests(TestCase):
    def test_needs_fuel_positive(self):
        car = Car()
        car.needsFuel = Mock()
        car.needsFuel.return_value = True
        carImpl = CarImpl(car)
        self.assertEqual(carImpl.needsFuel(), "car needs more fuel")
    
    def test_needs_fuel_negative(self):
        car = Car()
        car.needsFuel = Mock()
        car.needsFuel.return_value = False
        carImpl = CarImpl(car)
        self.assertEqual(carImpl.needsFuel(), "car doesn't need any fuel")
    

    def test_temperature(self):
        car = Car()
        car.getEngineTemperature = Mock()
        car.getEngineTemperature.return_value = 180
        carImpl = CarImpl(car)
        self.assertEqual(carImpl.getEngineTemperature(), "The engine's temperature is 180 °C")

    
    def test_temperature_unavailable(self):
        car = Car()
        car.getEngineTemperature = Mock()
        car.getEngineTemperature.return_value = None
        carImpl = CarImpl(car)
        self.assertEqual(carImpl.getEngineTemperature(), "Can't get the engine's temperature")

    def test_destination_Atlantyda(self):
        car = Car()
        car.driveTo = Mock()
        car.driveTo.return_value = "Atlantyda"
        carImpl = CarImpl(car)
        self.assertEqual(carImpl.driveTo("Atlantyda"), "Current destination is Atlantyda")

    
    def test_destination_name_with_space(self):
        car = Car()
        car.driveTo = Mock()
        car.driveTo.return_value = "New York"
        carImpl = CarImpl(car)
        self.assertEqual(carImpl.driveTo("New York"), "Current destination is New York")

    def test_destination_name_with_numbers(self):
        car = Car()
        car.driveTo = Mock()
        car.driveTo.return_value = "Area 51"
        carImpl = CarImpl(car)
        self.assertEqual(carImpl.driveTo("Area 51"), "Current destination is Area 51")

    
    def test_destination_not_set(self):
        car = Car()
        car.driveTo = Mock()
        car.driveTo.return_value = None
        carImpl = CarImpl(car)
        self.assertEqual(carImpl.driveTo(None), "The destination hasn't been set")
