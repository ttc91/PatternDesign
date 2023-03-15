
class Animal:
    name = None
    age = None
    species = None

    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def __str__(self):
        print("Name: " + str(self.name))
        print("Age: " + str(self.age))
        print("Species: " + str(self.species))

if __name__ == "__main__" :

    animal = Animal("Tina", 1, "Dog")
    animal.__str__()