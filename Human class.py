class Human:
    # Class attribute
    species = "Homo Sapiens"
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

x = Human("Samantha", 32, "Female")
y = Human("Rachel", 29, "Female")
print(x.age)
print(y.name)

