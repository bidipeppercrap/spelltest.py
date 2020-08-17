from spelltest.utils.attack import damage_dealt

class Creature:
    def __init__(self, name, health, energy, damage, defense):
       self.name = name
       self.health = self.health_limit = health
       self.energy = self.energy_limit = energy
       self.damage = damage
       self.defense = defense

    def __str__(self):
        return 'I\'m a creature'

    def attacked(self, damage):
        self.health -= damage_dealt(damage, self.defense)

    def attack(self, creature):
        creature.attacked(self.damage)
