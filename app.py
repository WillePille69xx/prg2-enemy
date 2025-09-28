class Enemy:
    def __init__(self, health, attack: int, name: str):
        self.health = health
        self.attack_power = attack
        self.name = name

    def attack(self):
        print(f"{self.name} attacks for {self.attack_power} damage!")
        
    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage! Remaining health: {self.health}")
        
    def print_status(self):
        print(f"Enemy: {self.name}, has {self.health} hp")
    
slime = Enemy(10, 5, "Slime")
slime.print_status()
slime.attack()
slime.take_damage(3)