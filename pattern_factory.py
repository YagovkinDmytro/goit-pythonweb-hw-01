from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self):
        pass

    @abstractmethod
    def create_motorcycle(self):
        pass

class USVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, f"{model} (US Spec)")
    
    def create_motorcycle(self, make, model):
        return Motorcycle(make, f"{model} (US Spec)")

class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, f"{model} (EU Spec)")
    
    def create_motorcycle(self, make, model):
        return Motorcycle(make, f"{model} (EU Spec)")

class Car(Vehicle):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        print(f"{self.make} {self.model}: Двигун запущено")

class Motorcycle(Vehicle):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        print(f"{self.make} {self.model}: Мотор заведено")


if __name__ == "__main__":
    vehicle1 = Car("Toyota", "Corolla")
    vehicle1.start_engine()

    vehicle2 = Motorcycle("Harley-Davidson", "Sportster")
    vehicle2.start_engine()

    us_factory = USVehicleFactory()
    vehicle3 = us_factory.create_car("Ford", "Mustang")
    vehicle3.start_engine()

    eu_factory = EUVehicleFactory()
    vehicle4 = eu_factory.create_motorcycle("Yamaha", "MT-07")
    vehicle4.start_engine()