class Human:
    def __init__(self, name="Human"):
        self.name = name

class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passangers = []

    def add_passenger(self, *human):
        for h in human:
            self.passangers.append(h)

    def printpass(self):
        if not self.passangers:
            print(f"Пасажири в авто {self.brand} не наявні")
            return
        else:
            print(f"В авто {self.brand} наявні пасажири:")
            for p in self.passangers:
                print(f"- ", p.name)

car = Auto("Toyota")
bob = Human("Bob")
kate = Human("Kate")
petro = Human("Petro")
car.add_passenger(bob, kate, petro)
print(car.passangers)
car.printpass()