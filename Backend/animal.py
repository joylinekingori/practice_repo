class Animal:
    def make_sound(self):
        pass
class Dog (Animal):
    def make_sound(self):
        print("wolf")
class Cat(Animal):
    def make_sound(self):
        print("meow")
    animals=[Cat(),Dog(),Cat(),Cat()]
    for animal in animals:
        animal make_sound()