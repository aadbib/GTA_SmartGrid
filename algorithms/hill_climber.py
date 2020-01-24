from copy import deepcopy
from random import choice

def hill_climber_algorithm(grid):
    """Algoritme die iteratief verbeteringen gaat toepassen d.m.v. de hillclimber methode"""

    # Prijzen van originele grid en grid_copy
    best_price_grid = grid.get_total_price()

    # Maak een deepcopy van de grid, en leeg de set van unieke kabels voor alle batterijen
    grid_copy = deepcopy(grid)
    grid_copy.clear_unique_cables_batteries()

    # Pak alle batterijen uit deze grid
    all_batteries = grid_copy.get_batteries()

    # Zorgt ervoor dat we huizen NIET uit dezelfde batterij gaan pakken en vergelijken
    all_indexes_all_batteries = [0, 1, 2, 3, 4]

    # Pak twee sets, onthoud alles
    battery1_index = choice(all_indexes_all_batteries)
    all_indexes_all_batteries.remove(battery1_index)
    battery1 = all_batteries[battery1_index]

    battery1_houses = battery1.get_houses()
    house1 = choice(battery1_houses)
    house1_index = battery1_houses.index(house1)

    battery2_index = choice(all_indexes_all_batteries)
    all_indexes_all_batteries.remove(battery2_index)
    battery2 = all_batteries[battery2_index]
    battery2_houses = battery2.get_houses()
    house2 = choice(battery2_houses)
    house2_index = battery2_houses.index(house2)

    # Verwijder de huizen uit de batteerij-huizen array dmv een index en verwijder de kabels van huis
    battery1.remove_house(house1_index)
    battery2.remove_house(house2_index)

    # Leg kabel vanuit batterij naar huis
    battery1.lay_cable_to_house(house2)
    battery2.lay_cable_to_house(house1)

    # Check of capaciteit overschreden wordt, nee: ga door ja: verwijder copy en stop
    if battery1.get_remaining() < 0 or battery2.get_remaining() < 0:

        # Verwijder object en leeg geheugen met del
        del grid_copy

        return None

    # Is de nieuwe resultaat beter? Ja: return resultaat Nee: verwijder copy en stop
    if grid_copy.get_total_price() < best_price_grid:
        return grid_copy

    # Todo: Bereken opnieuw kabel/batterij afstand, maar dan met geswitchte batterijen. Dus huis-1 batterij-2, huis-2 batterij-1
    # Todo: Hill_climber voor algoritme 3 of 8







