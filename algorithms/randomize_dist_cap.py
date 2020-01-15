# Todo: Upper en lower bound definieren
from .randomize import randomize_objects

def find_battery(batterijen, huis):
    """
    Zoekt het dichtstbijzijndste batterij voor een gegeven huis, waarbij de output in de resterende capaciteit past
    """
    optimale_index = 0
    min_afstand = 100
    output_huis = huis.get_output()

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

def dist_cap_algorithm(grid):
    """
    Algoritme die 'random' de huizen aan de zo dichtbijzijnste batterij aansluit, waarbij de output in de capaciteit past
    """
    huizen = grid.get_huizen()
    batterijen = grid.get_batterijen()

    randomize_objects(huizen, batterijen)

    for huis in huizen:
        batterij = find_battery(batterijen, huis)
        batterij.lay_cable_to_house(huis)