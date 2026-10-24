class Human:
    species = "Human"
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Привіт, мене звати {self.name}")

class Student(Human):
    def __init__(self, name, grp):
        super().__init__(name)
        self.grp = grp
    def study(self):
        print(f"{self.name} вчиться у групі {self.grp}")

class Worker(Human):
    def work(self):
        print(f"{self.name} працює")

s = Student("Olena", "ПЗ-21")
s.say_hello()
s.study()
w = Worker("Bob")
w.say_hello()
w.work()
print(s.species)