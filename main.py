import random


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

    def attack(self, unit, defense):
        damage = self._damage
        if random.random() < (self._percent_cp / 100):
            damage = self._critical_power
        damage -= damage * (defense / 100)
        unit._health -= damage


class Warrior(Unit):
    def __init__(self):
        super().__init__(health=100, damage=50, defense=50, critical_power=100, percent_cp=15)


class Mage(Unit):
    def __init__(self):
        super().__init__(health=100, damage=70, defense=20, critical_power=140, percent_cp=10)


class Archer(Unit):
    def __init__(self):
        super().__init__(health=100, damage=60, defense=10, critical_power=120, percent_cp=35)


class Game:
    def battle(self, unit1, unit2):
        if isinstance(unit1, Unit) and isinstance(unit2, Unit):
            print("Battle begins!")
            print(f"Unit 1: {unit1}")
            print(f"Unit 2: {unit2}")

            while True:
                print("--- Round ---")
                unit1.attack(unit1, unit2._defense)
                print(f"Unit 1 attacks Unit 2!")
                unit2.attack(unit2, unit1._defense)
                print(f"Unit 2 attacks Unit 1!")

                print(f"Unit 1: {unit1}")
                print(f"Unit 2: {unit2}")

                if self.is_battle_finished(unit1, unit2):
                    winner = self.is_battle_finished(unit1, unit2)
                    if winner:
                        print(f"{winner} wins!")
                    else:
                        print("It's a draw!")
                    break

    def is_battle_finished(self, unit1, unit2):
        if unit1._health <= 0 < unit2._health:
            return "Unit 2"
        elif unit2._health <= 0 < unit1._health:
            return "Unit 1"
        elif unit1._health <= 0 and unit2._health <= 0:
            return "Draw"


if __name__ == "__main__":
    game = Game()
    warrior = Warrior()
    mage = Mage()
    archer = Archer()

    game.battle(warrior, mage)
