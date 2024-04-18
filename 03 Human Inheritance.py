class Human: # Parent class
    # Class attribute
    species = "Homo Sapiens"
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def description(self):
        print(f"Hello, everyone! My name is {self.name}, I'm a {self.gender} and I'm {self.age} years old.")


class Boy(Human): # Child class
    def schoolName(self, schoolname):
        print(f"I study in {schoolname}")

b = Boy("Samantha", 32, "Female")
b.description()
b.schoolName("MIT")

