# Importeer libraries
from copy import deepcopy
from random import choice

class Hillclimber:
    """Hillclimber algoritme: iteratief verbeteringen toepassen"""

    @staticmethod
    def hill_climber_algorithm(grid):

        # Pak totale prijs grid, leeg unieke kabels, en kopieer batterijen
        best_price_grid = grid.get_total_price()
        grid_copy = deepcopy(grid)
        grid_copy.clear_unique_cables_batteries()
        all_batteries = grid_copy.get_batteries()

        # Voorkomt het pakken van huizen van zelfde batterij
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

        # Verwijder de huizen uit de batteerij-huizen array, en leg kabels
        battery1.remove_house(house1_index)
        battery2.remove_house(house2_index)
        battery1.lay_cable_to_house(house2)
        battery2.lay_cable_to_house(house1)

        # Check of capaciteit overschreden wordt, nee: ga door ja: verwijder copy en stop
        if battery1.get_remaining() < 0 or battery2.get_remaining() < 0:
            del grid_copy

            return None

        if grid_copy.get_total_price() < best_price_grid:
            return grid_copy