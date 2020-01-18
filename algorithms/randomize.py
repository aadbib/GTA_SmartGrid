# Importeer shuffle
from random import shuffle, choice

def randomize_objects(houses, batteries):
    """
    Schud de batterijen en huizen in de grid, om de volgorde te randomizen
    """
    shuffle(houses)
    shuffle(batteries)

def rand_one_to_one_algorithm(grid):
    """
    Algoritme die 'random' de huizen één op één aan een batterij aansluit
    """
    houses = grid.get_houses()
    batteries = grid.get_batteries()

    randomize_objects(houses, batteries)

    for house in houses:
        battery = choice(batteries)
        battery.lay_cable_to_house(house)