#Activity 2: Polymorphism Challenge! 
class Animal:
    def move(self):
        pass  # placeholder for polymorphism

class Dog(Animal):
    def move(self):
        print("Dog runs 🐕")

class Bird(Animal):
    def move(self):
        print("Bird flies 🕊️")

class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Car drives 🚗")

class Plane(Vehicle):
    def move(self):
        print("Plane flies ✈️")

# Example usage (Polymorphism in action)
animals = [Dog(), Bird()]
vehicles = [Car(), Plane()]

for a in animals:
    a.move()

for v in vehicles:
    v.move()
