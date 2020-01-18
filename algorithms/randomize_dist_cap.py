# Todo: Upper en lower bound definieren
from .randomize import randomize_objects

def find_battery(batteries, house):
    """
    Zoekt het dichtstbijzijndste batterij voor een gegeven huis, waarbij de output in de resterende capaciteit past
    """
    optimal_index = 0
    min_distance = 100
    output_house = house.get_output()

    for index, battery in enumerate(batteries):
        try:
            distance_battery = house.distance(battery)

            if distance_battery < min_distance:
                remaining = battery.get_remaining()

                if remaining >= output_house:
                    optimal_index = index
                    min_distance = distance_battery

        except IndexError:
            pass

    return batteries[optimal_index]

def dist_cap_algorithm(grid):
    """
    Algoritme die 'random' de huizen aan de zo dichtbijzijnste batterij aansluit, waarbij de output in de capaciteit past
    """
    houses = grid.get_houses()
    batteries = grid.get_batteries()

    randomize_objects(houses, batteries)

    for house in houses:
        battery = find_battery(batteries, house)
        battery.lay_cable_to_house(house)