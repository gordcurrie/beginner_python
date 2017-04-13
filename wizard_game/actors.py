import random


class Creature(object):
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return "Creature {} of level {}".format(self.name, self.level)

    def get_defensive_roll(self):
        return random.randint(1, 12) * self.level


class Wizard(Creature):

    def attack(self, creature):
        print('The wizard {} attacks {}!'.format(self.name, creature))
        my_roll = random.randint(1,12) * self.level
        creature_roll = creature.get_defensive_roll()

        print("You roll {}...".format(my_roll))
        print("The {} rolls {}".format(creature, creature_roll))

        if my_roll >= creature_roll:
            print("The wizard has defeated the {}!".format(creature.name))
            return True
        else:
            print("The wizard has been defeated:(")
            return False


class SmallAnimal(Creature):
    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        return base_roll / 2


class Dragon(Creature):
    def __init__(self, name, level, scaliness, breaths_fire):
        super().__init__(name, level)
        self.scaliness = scaliness
        self.breaths_fire = breaths_fire

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        fire_modifier = 5 if self.breaths_fire else 1
        scale_modifier = self.scaliness / 10
        return base_roll * fire_modifier * scale_modifier