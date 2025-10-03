import time

class Enemy:
    def __init__(self, health, attack: int, name: str):
        self.health = health
        self.attack_power = attack
        self.name = name

    def attack(self, target: 'Enemy'):
        print(f"{self.name} attacks {target.name} for {self.attack_power} damage!")
        
    def take_damage(self, damage: int):
        self.health -= damage
        print(f"{self.name} takes {damage} damage! Remaining health: {self.health}")
        
    def print_status(self):
        print(f"Enemy: {self.name}, has {self.health} hp")
    
# Create two enemies
slime = Enemy(100, 20, "Slime")
dino = Enemy(100, 17, "Dino")
# slime.print_status()
# dino.print_status()
# dino.attack(slime)
# slime.take_damage(dino.attack_power)
# slime.print_status()

# loop their combat until one of them dies
def combat(slime: Enemy, dino: Enemy):
    while slime.health > 0 and dino.health > 0:
        dino.attack(slime)
        slime.take_damage(dino.attack_power)
        time.sleep(1)
        if slime.health <= 0:
            print(f"{slime.name} has been defeated!")
            break
        else:
            slime.attack(dino)
            dino.take_damage(slime.attack_power)
            time.sleep(1)
            if dino.health <= 0:
                print(f"{dino.name} has been defeated!")
                break
        time.sleep(1)
    slime.print_status()
    dino.print_status()
combat(slime, dino)