# Importeer shuffle
from random import shuffle, choice

def randomize_objects(huizen, batterijen):
    """
    Schud de batterijen en huizen in de grid, om de volgorde te randomizen
    """
    shuffle(huizen)
    shuffle(batterijen)

def rand_algorithm(grid):
    """
    Algoritme die 'random' de huizen aan een batterij aansluit
    """
    huizen = grid.get_huizen()
    batterijen = grid.get_batterijen()
    randomize_objects(huizen, batterijen)

    # Sluit alles random aan tot alle huizen aangesloten zijn
    while grid.is_everything_connected() is not True:
        huis = choice(huizen)
        batterij = choice(batterijen)
        batterij.lay_cable(huis)

def rand_one_to_one_algorithm(grid):
    """
    Algoritme die 'random' de huizen één op één aan een batterij aansluit
    """
    huizen = grid.get_huizen()
    batterijen = grid.get_batterijen()

    randomize_objects(huizen, batterijen)

    for huis in huizen:
        batterij = choice(batterijen)
        batterij.lay_cable(huis)