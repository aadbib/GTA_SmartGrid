# Todo: Upper en lower bound definieren
from .randomize import randomize_objects
from copy import deepcopy

def find_house(battery, houses):
    """
    Zoekt het dichtstbijzijndste huis voor een gegeven batterij, waarbij de output in de resterende capaciteit past
    """
    optimal_index = None
    min_distance = 100

    for index, house in enumerate(houses):
        output_house = house.get_output()

        try:
            distance_house = house.distance(battery)

            if distance_house < min_distance:
                remaining = battery.get_remaining()

                if remaining >= output_house:
                    optimal_index = index
                    min_distance = distance_house

        except IndexError:
            pass

    # Als de output niet meer voloet, return dan niks (en niet de 1e huis van huizen met index 0)
    try:
        house = houses[optimal_index]

        # Pop als deze huis geen exception throwed/raised
        houses.pop(optimal_index)
        return house

    except:
        pass

# Todo: Er is een probleem... Stel een andere batterij begint eerst, dan steeltie huis van andere batterij
def bat_dist_cap_algorithm(grid):
    """
    Algoritme die 'random' de batterijen aan de zo dichtbijzijnste huizen aansluit, waarbij de output in de capaciteit past
    """
    houses = grid.get_houses()
    batteries = grid.get_batteries()

    randomize_objects(houses, batteries)

    houses_copy = deepcopy(houses)

    for battery in batteries:

        # Batterij blijft huizen toevoegen tot find_house niks returned, oftewel batterij vol
        while True:
            house = find_house(battery, houses_copy)

            if house is not None:
                battery.lay_cable_to_house(house)

            else:
                break