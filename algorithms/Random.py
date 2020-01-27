# Importeer libraries
from random import choice
from functions.random import randomize_objects

class Random:
    """Random Algoritme"""

    @staticmethod
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