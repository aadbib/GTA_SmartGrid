def find_best_battery(batterijen, huis):
    """
    Zoekt de verste batterij voor een gegeven huis, waarbij de output niet uitmaakt
    """
    optimale_index = 0
    min_afstand = 101

    for index, batterij in enumerate(batterijen):
        try:
            afstand_batterij = huis.distance(batterij)

            if afstand_batterij < min_afstand:
                optimale_index = index
                min_afstand = afstand_batterij

        except IndexError:
            pass

    return batterijen[optimale_index]


def best_dist(grid):
    """
    Algoritme die de slechtse batterij voor een huis linkt
    """
    huizen = grid.get_huizen()
    batterijen = grid.get_batterijen()
    for huis in huizen:
        batterij = find_best_battery(batterijen, huis)
        batterij.lay_cable_to_house(huis)
