animal_list = [
    {
        "id": 1,
        "name": "Max",
        "species": "Dog",
        "age": 5,
        "sex": "Male",
        "mother": 7,
        "father": 4,
        "notes": "Very energetic, loves to play fetch."
    },
    {
        "id": 2,
        "name": "Whiskers",
        "species": "Cat",
        "age": 7,
        "sex": "Female",
        "mother": 8,
        "father": 5,
        "notes": "Enjoys sunbathing and chasing mice."
    },
    {
        "id": 3,
        "name": "Nemo",
        "species": "Fish",
        "age": 1,
        "sex": "Male",
        "mother": 9,
        "father": 6,
        "notes": "Swims very fast, lives in a freshwater aquarium."
    },
    # Second Generation
    # Father
    {
        "id": 4,
        "name": "Buddy",
        "species": "Dog",
        "age": 8,
        "sex": "Male",
        "mother": 10,
        "father": 11,
        "notes": "Loves to play with children."
    },
    {
        "id": 5,
        "name": "Fluffy",
        "species": "Cat",
        "age": 9,
        "sex": "Male",
        "mother": "Tiger",
        "father": "Snowball",
        "notes": "Loves to cuddle."
        
    },
    {
        "id": 6,
        "name": "Marlin",
        "species": "Fish",
        "age": 3,
        "sex": "Male",
        "mother": "Molly",
        "father": "Finn",
        "notes": "Adventurous and protective"
    },
    # Mothers
    {
        "id": 7,
        "name": "Lucy",
        "species": "Dog",
        "age": 10,
        "sex": "Female",
        "mother": "Maggie",
        "father": "Buddy Sr.",
        "notes": "The fastest dog in the park."
    },
    {
        "id": 8,
        "name": "Mittens",
        "species": "Cat",
        "age": 11,
        "sex": "Female",
        "mother": "Snowball",
        "father": "Oreo",
        "notes": "Has a playful personality."
    },
    {
        "id": 9,
        "name": "Coral",
        "species": "Fish",
        "age": 2,
        "sex": "Female",
        "mother": "Luna",
        "father": "Leo",
        "notes": "Beautiful and caring"
    },
    
    #3rd gen (grandparents)
    {   
        "id": 10,
        "name": "Sadie",
        "species": "Dog",
        "age": 10,
        "sex": "Female",
        "mother": " ",
        "father": " ",
        "notes": "Very friendly and loves to play."
    },
    
    {   
        "id": 11,
        "name": "Jake",
        "species": "Dog",
        "age": 12,
        "sex": "Male",
        "mother": " ",
        "father": " ",
        "notes": "Playful and friendly."
    },
]

class Animals:
    def __init__(self, id, name, species, age, sex, mother, father, notes):
        self.id = id
        self.name = name
        self.species = species
        self.age = age
        self.sex = sex
        self.mother = mother
        self.father = father
        self.notes = notes
        
    # def get_parents(self, child_name):
    #     if child_name == self.name:
    #         return self.father and self.mother
    #     else:
    #         return None
            
    
animals = [Animals(**data) for data in animal_list]

#loop through list to match id to animal ids to list and return the name of the matched animal
def get_parents(animal_id):
    for animal in animals:
        if animal.id == animal_id:
            return animal.name
        elif animal.id != animal_id:
            continue
        else:
            return "Unknown"
        
        
#print generations
def return_parents(animal_name): 
    for animal in animals:
        if animal.name == animal_name:
            f = get_parents(animal.father)
            m = get_parents(animal.mother)
            print(f"{animal.name}'s father is {f} and mother is {m}!\n")
            #recursion lol
            return_parents(f)
            return_parents(m)

# start prompt
def start_prompt():
    name = input("name?").capitalize()
    return_parents(name)
    
start_prompt()


