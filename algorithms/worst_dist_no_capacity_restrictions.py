def find_worst_battery(batterijen, huis):
    """
    Zoekt de verste batterij voor een gegeven huis, waarbij de output niet uitmaakt
    """
    slechtste_index = 0
    max_afstand = 0

    for index, batterij in enumerate(batterijen):
        try:
            afstand_batterij = huis.distance(batterij)

            if afstand_batterij > max_afstand:
                slechtste_index = index
                max_afstand = afstand_batterij

        except IndexError:
            pass

    return batterijen[slechtste_index]


def worst_dist(grid):
    """
    Algoritme die de slechtse batterij voor een huis linkt
    """
    huizen = grid.get_huizen()
    batterijen = grid.get_batterijen()
    for huis in huizen:
        batterij = find_worst_battery(batterijen, huis)
        batterij.lay_cable_to_house(huis)
