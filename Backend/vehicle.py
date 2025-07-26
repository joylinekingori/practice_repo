class Vehicle:
    def __init__(self,make,model):
        self.make=make
        self.model=model
    def start(self):
        print("The engine has started")
class Car(Vehicle):
    def __init__(self,make,model,colour):
         super().__init__(make,model)
         self.colour=colour
    def reverse(self):
        print("The car is reversing")
class Lory(Vehicle):
    def __init__(self,make,model,capacity):
        self.capacity=capacity
    def unload(self):
        print("The lory is unloading")