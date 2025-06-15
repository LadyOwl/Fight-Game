import random
import time

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        damage = self.attack_power
        other.health -= damage
        print(f"{self.name} атакует {other.name} и наносит {damage} урона!")

    def is_alive(self):
        return self.health > 0

    def status(self):
        return f"{self.name}: {max(self.health, 0)} HP"


class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        print("\nИгра началась!")
        print(self.player.status())
        print(self.computer.status())
        print("-" * 30)

        while self.player.is_alive() and self.computer.is_alive():
            input("\nНажмите Enter, чтобы атаковать...")
            self.player.attack(self.computer)
            print(self.computer.status())

            if not self.computer.is_alive():
                print("\nВы победили! 🎉")
                break

            time.sleep(1)

            print("\nКомпьютер атакует...")
            time.sleep(1)
            self.computer.attack(self.player)
            print(self.player.status())

            if not self.player.is_alive():
                print("\nВы проиграли. Компьютер победил. 💀")
                break

        print("-" * 30)
        print("Игра окончена.")

if __name__ == "__main__":
    player_name = input("Введите имя вашего героя: ")
    game = Game(player_name)
    game.start()


