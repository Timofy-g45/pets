class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50

    def feed(self):
        print(f"{self.name} поїв!")
        self.hunger += 50
        if self.hunger < 0:
            self.hunger = 0

    def status(self):
        print(f"{self.name} голод: {self.hunger}")

my_pet = Pet("мурзик")
my_pet.status()
my_pet.feed()
my_pet.status()
