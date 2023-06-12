class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def get_name(self):
        self.name
        print(f"Nama : {self.name}")
    def get_age(self):
        self.age
        print(f"Umur : {self.age}")
    def get_salary(self):
        self.salary
        print(f"Upah : {self.salary}")
class Manager(Employee):
    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary)
        self.department = department
    def get_department(self):
        self.department
        print(f"departement : {self.department}")
class Programmer(Employee):
    def __init__(self, name, age, salary, language):
        super().__init__(name, age, salary)
        self.language = language
    def get_language(self):
        self.language
        print(f"Bahasa Pemrograman : {self.language}")
# Hierarchical Inheritance
class SeniorProgrammer(Programmer):
    def __init__(self, name, age, salary, language, level):
        super().__init__(name, age, salary, language)
        self.level = level
    def get_level(self):
        self.level
        print(f"Level : {self.level}")
A=SeniorProgrammer("Arya Ghiffari",23,"Rp.23000000","python","max")
A.get_name()
A.get_age()
A.get_salary()
A.get_language()
A.get_level()