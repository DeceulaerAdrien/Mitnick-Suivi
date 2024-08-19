class Becodian:
    def __init__(self, name, is_staff_member):
        self.name = name
        self.is_staff_member = is_staff_member

    def introduce_becodian(self):
        if self.is_staff_member:
            return f"{self.name} is a staff member!"
        else:
            return f"{self.name} is a learner!"



class Learner(Becodian):
    def __init__(self, name,promotion):
        super().__init__(name, is_staff_member=False)
        self.promotion = promotion
    def introduce_learner(self):
        return self.introduce_becodian() + f"from {self.promotion}"



ludo = Becodian("ludo", True)
print(ludo.introduce_becodian())

jeremy = Learner("Jeremy", "Bouman 1")
print(jeremy.introduce_learner())

giuliano = Learner("Giuliano", "Bouman 1")
print(giuliano.introduce_learner())

mathieu = Learner("Mathieu", "Bouman 1")
print(mathieu.introduce_learner())

geoffrey = Learner("Geoffrey", "Bouman 1")
print(geoffrey.introduce_learner())

adrien = Learner("Adrien", "Woods 1")
print(adrien.introduce_learner())