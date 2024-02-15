class Animals:
    def __init__(self, name, species, color, age, sex):
        self.name = name
        self.species = species
        self.color = color
        self.age = age
        self.sex = sex


    def get_species(self):
        if self.species == " ":
            return "Unknown"
        else:
            return self.species

animal_list = [
    {"name": "Fido", "species": " ", "color": "Brown", "age": 3, "sex": "Male"},
    {"name": "Whiskers", "species": "Cat", "color": "Gray", "age": 5, "sex": "Female"},
    {"name": "Nemo", "species": "Fish", "color": "Orange", "age": 1, "sex": "Male"},
    {"name": "Bella", "species": "Dog", "color": "White", "age": 2, "sex": "Female"},
    {"name": "Stripey", "species": "Zebra", "color": "Black and White", "age": 4, "sex": "Male",
    },
]

animals = [Animals(**data).get_species() for data in animal_list]

def return_species():
    i = int(input("index?"))
    try:
        print(animals[i-1])
    except IndexError :
        return print(False)
        

return_species()