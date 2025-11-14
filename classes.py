class Vehicle:
    WHEELS_DEFAULT = 4

    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.is_running = False 
    
    def start_engine(self):
        if not self.is_running:
            self.is_running = True
            return f"The {self.color} {self.make} {self.model}'s engine started."
        else:
            return "The engine is already running."
    
    def get_info(self):
        return f"Vehicle: {self.year} {self.make} {self.model}, Color: {self.color}, Wheels: {Vehicle.WHEELS_DEFAULT}"

car1 = Vehicle("Toyota", "Camry", 2020, "Silver")
truck = Vehicle("Ford", "F-150", 2023, "Black")
print(car1.get_info())
print(truck.start_engine())
print(f"Car 1's running status: {car1.is_running}")

class Motorcycle(Vehicle): 
    WHEELS_DEFAULT = 2

    def __init__(self, make, model, year, color, has_sidecar):
        super().__init__(make, model, year, color)
        self.has_sidecar = has_sidecar

    def lean_into_turn(self):
        return f"The {self.model} is leaning into the turn."
    
    # Override a parent method (Polymorphism)
    def get_info(self):
        base_info = super().get_info()
        return f"{base_info} | Sidecar: {self.has_sidecar}"

# Creating a Motorcycle Object
bike = Motorcycle("Harley-Davidson", "Iron 883", 2018, "Matte Gray", False)

print("\n--- Inheritance Example ---")
print(bike.start_engine())        
print(bike.lean_into_turn())      
print(bike.get_info())            
print(f"Bike Wheels: {bike.WHEELS_DEFAULT}") 
