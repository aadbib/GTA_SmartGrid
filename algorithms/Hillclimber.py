from copy import deepcopy
from functions.switcher import switch_houses_hillclimber

class Hillclimber:
    """Hillclimber algoritme: iteratief verbeteringen toepassen"""

    @staticmethod
    def hill_climber_algorithm(grid):

        # Pak totale prijs grid, leeg unieke kabels, en kopieer batterijen
        best_price_grid = grid.get_total_price()
        grid_copy = deepcopy(grid)
        grid_copy.clear_unique_cables_batteries()
        all_batteries = grid_copy.get_batteries()

        # Voorkom huizen van zelfde batterij
        all_indexes_all_batteries = [0, 1, 2, 3, 4]
        battery1, battery2 = switch_houses_hillclimber(all_indexes_all_batteries, all_batteries)

        # Check of capaciteit overschreden wordt, nee: ga door ja: verwijder copy en stop
        if battery1.get_remaining() < 0 or battery2.get_remaining() < 0:
            del grid_copy

            return None

        if grid_copy.get_total_price() < best_price_grid:
            return grid_copy