class Human:
    # Class attribute
    species = "Homo Sapiens"
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
# x, y are instances of class Human
x = Human("Samantha", 32, "Female")
y = Human("Rachel", 29, "Female")

print(x.species) # species are class attributes, hence will have same value for all instances
print(y.species)

# name, gender and age will have different values per instance, because they are instance attributes
print(f"Hi! My name is {x.name}. I'm {x.age} years old and I'm {x.gender}")
print(f"Hi! My name is {y.name}. I'm {y.age} years old and I'm {y.gender}")


