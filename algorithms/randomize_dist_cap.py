# Importeer shuffle
from random import shuffle

# Todo: Upper en lower bound definieren

def randomize_objects(grid):
    """
    Schud de batterijen en huizen in de grid, om de volgorde te randomizen
    """
    shuffle(grid.get_batterijen())
    shuffle(grid.get_huizen())

def find_battery(grid, huis):
    """
    Zoekt het dichtstbijzijndste batterij voor een gegeven huis
    """
    optimale_index = 0
    min_afstand = 100
    output_huis = huis.get_output()

    batterijen = grid.get_batterijen()

    for index, batterij in enumerate(batterijen):
        try:
            afstand_batterij = huis.distance(batterij)

            if afstand_batterij < min_afstand:
                resterend = batterij.get_resterend()

                if resterend >= output_huis:
                    optimale_index = index
                    min_afstand = afstand_batterij

        except IndexError:
            pass

    return batterijen[optimale_index]

def lay_cables(grid):
    """
    Algoritme die 'random' de huizen aan de zo dichtbijzijnste batterij aansluit
    """
    huizen = grid.get_huizen()
    batterijen = grid.get_batterijen()

    shuffle(huizen)
    shuffle(batterijen)

    for huis in huizen:
        batterij = find_battery(grid, huis)

        distance_y = int(batterij.get_locatie()[1]) - int(huis.get_locatie()[1])
        distance_x = int(batterij.get_locatie()[0]) - int(huis.get_locatie()[0])
        huis_y = int(huis.get_locatie()[1])
        huis_x = int(huis.get_locatie()[0])
        batterij_y = int(batterij.get_locatie()[1])

        if distance_y > 0:

            for movement in range(abs(distance_y)):
                huis.set_kabels((huis_x, huis_y + movement))
        else:

            for movement in range(abs(distance_y)):
                huis.set_kabels((huis_x, huis_y - movement))

        if distance_x > 0:

            for movement in range(abs(distance_x) + 1):
                huis.set_kabels((huis_x + movement, batterij_y))
        else:

            for movement in range(abs(distance_x) + 1):
                huis.set_kabels((huis_x - movement, batterij_y))

        batterij.set_huis(huis)