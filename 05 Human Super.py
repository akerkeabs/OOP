class Human: # Parent class
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def description(self):
        print(f"Hello, everyone! My name is {self.name}, I'm a {self.gender} and I'm {self.age} years old.")

    def code(self):
        print("I can code.")

class Girl(Human): # Child class
    def codecode(self):
        print("I can teach.")
    def activity(self):
        super().code()

g = Girl("Samantha", 32, "Girl")
g.description()
g.activity()

