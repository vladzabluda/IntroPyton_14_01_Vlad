class Unit:
    def __init__(self, name, clan):
        self.name = name
        self.clan = clan
        self.max_health = 100
        self.min_health = 1
        self.max_strength = 10
        self.min_strength = 1
        self.max_a = 10
        self.min_a = 1
        self.max_i = 10
        self.min_i = 1
    def read_unit(self):
        read = self.name + " " + self.clan
        return read.title()
    def read_health(self):
        if self.min_health + 10 > self.max_health:
            self.max_health = 100
        else:
            self.min_i += 10
    def health_read(self):
        print("In object: " + " health")
class Mage(Unit):
    def __init__(self, name, clan, air, fire, water):
        super().__init__(name, clan)
        self.air = air
        self.fire = fire
        self.water = water
    def intelligence_magic(self):
        if self.min_i + 1 < self.max_i:
            self.min_i = 10
        else:
            self.min_i += 10
class Archer(Unit):
    def __init__(self, name, clan, bow, crossbow):
        super().__init__(name, clan)
        self.bow = bow
        self.crossbow = crossbow

    def a_luchnyk(self):
        if self.min_a + 1 < self.max_a:
            self.max_a = 10
        else:
            self.min_a += 10
class Knight(Unit):
    def __init__(self, name, clan, sword, axe, pike):
        super().__init__(name, clan)
        self.sword = sword
        self.axe = axe
        self.pike = pike
    def a_lyzary(self):
        if self.min_strength + 1 < self.max_strength:
            self.max_strength = 10
        else:
            self.min_strength += 10

erifan = Mage("Erifan", "Dragon", "fire", "water", "air")
print(erifan.read_unit())
print(erifan.name)
print(erifan.clan)
eren = Archer("Eren", "Fresh", "crossbow", "bow")
print(eren.read_unit())
print(eren.clan)
print(eren.name)
selfi = Knight("Selfi", "Archer_best", "sword", "axe", "pike")
print(selfi.read_unit())
print(selfi.clan)
print(selfi.max_strength)
print(selfi.min_strength)
print(selfi.name)
print(selfi.max_i)
print(selfi.max_health)
selfi.health_read()
selfi.a_lyzary()