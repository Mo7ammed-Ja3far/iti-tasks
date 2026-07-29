class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self, target):
        damage = 10
        print(f"{self.name} attacks {target.name} for {damage} damage.")
        target.take_damage(damage)

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} took {damage} damage. Health left: {self.health}")

    def is_alive(self):
        return self.health > 0


class Warrior(Character):
    def __init__(self, name, health, armor):
        super().__init__(name, health)
        self.armor = armor

    def attack(self, target):
        damage = 20
        print(f"{self.name} slashes {target.name} with a sword!")
        target.take_damage(damage)

class Wizard(Character):
    def __init__(self, name, health, mana):
        super().__init__(name, health)
        self.mana = mana

    def attack(self, target):
        damage = 25
        self.mana -= 10
        print(f"{self.name} casts a fireball at {target.name}!")
        target.take_damage(damage)


class Archer(Character):
    def __init__(self, name, health, arrows):
        super().__init__(name, health)
        self.arrows = arrows

    def attack(self, target):
        if self.arrows > 0:
            self.arrows -= 1
            damage = 18
            print(f"{self.name} shoots an arrow at {target.name}!")
        else:
            damage = 5
            print(f"{self.name} has no arrows left and hits {target.name} with the bow!")

        target.take_damage(damage)

def battle(player1, player2):
    print(f"\n- Battle: {player1.name} vs {player2.name}")

    while player1.is_alive() and player2.is_alive():
        player1.attack(player2)
        if not player2.is_alive():
            break
        player2.attack(player1)

    winner = player1 if player1.is_alive() else player2
    print(f"\nWinner: {winner.name}!")

if __name__ == "__main__":
    warrior = Warrior("Thorin", 100, armor=10)
    wizard = Wizard("Gandalf", 80, mana=50)
    archer = Archer("Legolas", 90, arrows=2)

    print("- Demonstrating Polymorphism")
    heroes = [warrior, wizard, archer]
    dummy = Character("Training Dummy", 100)

    for hero in heroes:
        hero.attack(dummy)
    battle(warrior, wizard)