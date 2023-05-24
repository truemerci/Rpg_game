class Unit:
    def __init__(self, health, damage, defense, critical_power, percent_cp):
        self.health = health
        self.damage = damage
        self.defense = defense
        self.critical_power = critical_power
        self.percent_cp = percent_cp

    def __str__(self):
        characteristic = f"Health: {self.health}, damage: {self.damage}, defense: {self.defense}, " \
                         f"critical power: {self.critical_power}, percent critical power: {self.percent_cp}% "
        return characteristic


class Warrior(Unit):
    pass


class Mage(Unit):
    pass


class Archer(Unit):
    pass


warrior = Warrior(100, 50, 50, 100, 15)
mage = Mage(100, 70, 20, 140, 8)
archer = Archer(100, 60, 15, 120, 50)
