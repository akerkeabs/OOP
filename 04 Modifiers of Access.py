# Direct access modifiers like public, private, and protected don't
# exist in Python.
# Protected class is represented by a single underscore ( ) _.
# Private class is denoted by a double underscore __.
class Employee:
    def __init__(self, name, employeeId, salary):
        self.name = name # making employee name public
        self._empId = employeeId # making employee ID protected
        self.__salary = salary # making salary private

    def getSalary(self):
        print(f"The salary of Employee is {self.__salary}")

employee1 = Employee('Jungkook', '96969696', '$120000')
print(f"Employee's name is {employee1.name}")
print(f"Employee's ID is {employee1._empId}")
print(f"Employee's salary is {employee1.salary}")