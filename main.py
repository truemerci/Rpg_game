class Unit:
    def __init__(self, health, damage, defense, critical_power, percent_cp):
        self._health = health
        self._damage = damage
        self._defense = defense
        self._critical_power = critical_power
        self._percent_cp = percent_cp

    def __str__(self):
        characteristic = f"Health: {self._health}, damage: {self._damage}, defense: {self._defense}, " \
                         f"critical power: {self._critical_power}, percent critical power: {self._percent_cp}%"
        return characteristic


class Warrior(Unit):
    def __init__(self):
        super().__init__(health=100, damage=50, defense=50, critical_power=100, percent_cp=15)


class Mage(Unit):
    def __init__(self):
        super().__init__(health=100, damage=70, defense=20, critical_power=140, percent_cp=10)


class Archer(Unit):
    def __init__(self):
        super().__init__(health=100, damage=60, defense=10, critical_power=120, percent_cp=35)
