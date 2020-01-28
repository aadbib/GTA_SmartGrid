from random import shuffle

def randomize_objects(houses, batteries):
    """Schud de batterijen en huizen in de grid, om de volgorde te randomizen"""

    shuffle(houses)
    shuffle(batteries)