class Human:
    # Class attribute
    species = "Homo Sapiens"
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    # Instance method
    def speak(self):
        return f"Hello, everyone! My name is {self.name}"

    # Instance method
    def eat(self, favouriteDish):
        return f"I love to eat {favouriteDish}!!!"

x = Human("Samantha", 32, "Female")
print(x.speak())
print(x.eat("Pizza"))