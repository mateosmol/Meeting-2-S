# print("Hello!")
#
# name = "Matvij"
# print(name)
#
# age = int(input("age? "))
# print(age)

class Student:
    def __init__(self, name="Антайтлд", height="Нот а намбер"):
        self.name = name
        self.height = height

    def grow(self, cm):
        self.height = int(self.height)
        self.height += cm
        print(f"{self.name} виріс, зріст {self.height}")

    def __str__(self):
        return f"Студент {self.name}, його зріст {self.height}"

    def __del__(self):
        print(f"Студента {self.name} видалено!")

bob = Student("Bob", "175")
print(bob.height, bob.name)
bob.grow(10)
print(bob)

del bob
kate = Student("Katyunya", "milipi")

