class Superhero:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"{self.name} uses {self.power}!")

class FlyingHero(Superhero):
    def attack(self):
        print(f"🦸 {self.name} flies into the sky and attacks with {self.power}!")

class SpeedHero(Superhero):
    def attack(self):
        print(f"⚡ {self.name} runs at lightning speed and attacks with {self.power}!")

hero1 = FlyingHero("SkyMan", "Thunder Blast")
hero2 = SpeedHero("FlashBolt", "Speed Punch")

print("===== SUPERHERO BATTLE =====\n")

hero1.attack()
hero2.attack()

print("\nBattle Finished!")
