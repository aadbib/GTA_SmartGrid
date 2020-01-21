from copy import deepcopy
from random import choice

def hill_climber_algorithm(grid):
    """Algoritme die iteratief verbeteringen gaat toepassen d.m.v. de hillclimber methode"""

    # Maak een deepcopy van de grid, en leeg de set van unieke kabels voor alle batterijen
    grid_copy = deepcopy(grid)
    grid_copy.clear_unique_cables_batteries()

    # Pak alle batterijen uit deze grid
    all_batteries = grid_copy.get_batteries()

    for b in all_batteries:

        # Todo: In hillclimber moet je niet dezelfde oplossingen gaan vergelijken, bv huis1, batterij1 vs huis2, batterij 2.
        # Todo: Zoek uit hoe je geen sets die al vergeleken zijn, niet opnieuw met elkaar vergelijkt?

        # Zorgt ervoor dat we huizen NIET uit dezelfde batterij gaan pakken en vergelijken
        all_indexes_all_batteries = [0, 1, 2, 3, 4]

        # Pak twee sets, en onthoud alles
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

        # Todo: Pak de kabels/coordinaten van deze huizen, leeg ze, en haal de huizen weg van hun batterijen_array
        # Todo: Bereken opnieuw kabel/batterij afstand, maar dan met geswitchte batterijen. Dus huis-1 batterij-2, huis-2 batterij-1







