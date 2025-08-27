#Assignment 1: Design Your Own Class!
# Base Class
class Smartphone:
    def __init__(self, brand, model, storage, battery_level=100):
        self.brand = brand
        self.model = model
        self.storage = storage  
        self.battery_level = battery_level  

    def charge(self, amount):
        self.battery_level = min(100, self.battery_level + amount)
        print(f"{self.model} charged. Battery level: {self.battery_level}%")

    def use(self, hours):
        drain = hours * 10  # 10% battery drain per hour
        self.battery_level = max(0, self.battery_level - drain)
        print(f"Used {self.model} for {hours} hour(s). Battery level: {self.battery_level}%")

    def check_status(self):
        print(f"{self.brand} {self.model} - Storage: {self.storage}GB, Battery: {self.battery_level}%")

# Child Class (Inheritance)
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, battery_level=100, cooling_system=True):
        super().__init__(brand, model, storage, battery_level)
        self.cooling_system = cooling_system

    def play_game(self, hours):
        drain = hours * 20  # Gaming drains faster
        self.battery_level = max(0, self.battery_level - drain)
        print(f"Played game on {self.model} for {hours} hour(s). Battery level: {self.battery_level}%")

# Example usage
phone1 = Smartphone("Samsung", "Galaxy S24", 256)
phone2 = GamingPhone("Asus", "ROG Phone 8", 512)

phone1.check_status()
phone1.use(2)
phone1.charge(15)

phone2.check_status()
phone2.play_game(1)
