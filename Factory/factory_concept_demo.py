from abc import ABC,abstractmethod

class VehicleInterface(ABC):
    @staticmethod
    @abstractmethod
    def get_vehicle_type():
        pass

class ElectricVehicle(VehicleInterface):
    def __init__(self):
        self.name='Electric Vehicle'
    def get_vehicle_type(self):
        return self

class PetrolVehicle(VehicleInterface):
    def __init__(self):
        self.name="Petrol Vehicle"
    def get_vehicle_type(self):
        return self

class DieselVehicle(VehicleInterface):
    def __init__(self):
        self.name="Diesel Vehicle"
    def get_vehicle_type(self):
        return self
class VehicleFactory():
    @staticmethod
    def create_object(some_condition):
        if some_condition=='E':
            return ElectricVehicle()
        elif some_condition=='P':
            return PetrolVehicle()
        elif some_condition=='D':
            return DieselVehicle()
#main
product = VehicleFactory.create_object('D')
print(product.name)
