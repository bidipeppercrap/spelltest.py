def damage_multiplier(defense):
    return 1 - ((0.052 * defense) / (0.9 + (0.048 * defense)))

def damage_dealt(damage, defense):
    return damage * damage_multiplier(defense)

