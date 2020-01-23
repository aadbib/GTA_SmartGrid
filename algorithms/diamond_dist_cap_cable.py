from models.Segment import Segment
from copy import deepcopy
from algorithms.bat_randomize_dist_cap import find_house

def segmenting_grid(grid):
    starting_x = 0
    starting_y = 0

    batteries = deepcopy(grid.get_batteries())
    grid.clear_batteries()

    # Leeg grid batterijen
    deleted = []

    while starting_y < 50:
        while starting_x < 50:

            segment = Segment((starting_x, starting_y), (starting_x + 10, starting_y + 10))

            for battery in batteries:

                battery_location = battery.get_location()
                battery_x = int(battery_location[0])
                battery_y = int(battery_location[1])

                if (battery_x >= starting_x and battery_x <= (starting_x + 10)) and (
                        battery_y >= starting_y and battery_y <= (starting_y + 10)):

                    if battery not in deleted:
                        segment.set_battery(battery)
                        deleted.append(battery)

            grid.set_segment(segment)
            starting_x += 10

        starting_x = 0
        starting_y += 10

    deleted.clear()

def diamond_bat_dist_cap(grid):
    """
    Algoritme die 'random' de batterijen aan de zo dichtbijzijnste huizen aansluit, waarbij de output in de capaciteit past
    """
    houses = grid.get_houses()
    batteries = grid.get_batteries()

    houses_copy = deepcopy(houses)

    for battery in batteries:

        # Batterij blijft huizen toevoegen tot find_house niks returned, oftewel batterij vol
        while True:
            house = find_house(battery, houses_copy)

            # Todo: Check of is not None weg kan
            if house is not None:
                battery.set_house(house)

            else:
                break

def diamond_sorting_batteries(grid):
    segment_order = [0, 20, 24, 4, 1, 5, 15, 21, 23, 19, 9, 3, 2, 6, 10, 16, 22, 18, 14, 8, 7, 11, 17, 13, 12]

    grid_segmenten = grid.get_segmenten()

    for order in segment_order:
        segment = grid_segmenten[order]

        # todo: CHECK OF is not None eruit kan
        if segment.get_battery() is not None:
            battery = segment.get_battery()
            grid.set_battery(battery)

def diamond_lay_cables(grid):
    """
    Algoritme die ook naar bestaande gelegde kabels kijkt, en de de kabel/batterij kiest met minste afstand
    """
    # houses = grid.get_houses()
    batteries = grid.get_batteries()

    # randomize_objects(houses, batteries)

    # Voor batterij in batterijen
    for battery in batteries:
        houses = battery.get_houses()

        for house in houses:

            # Bereken de afstand tussen de beste batterij en huis
            distance_battery = house.distance(battery)

            # Base-line afstand kabel (Upper-bound)
            best_distance_cable = 1000000

            # Declaratie beste kabel
            best_cable = tuple

            # Als de batterij uberhaupt verbindingen heeft, anders prune
            if not battery.is_empty():

                # Pak de unieke kabels die aan de batterij is aangesloten
                cables = battery.get_unique_cables()

                # Loop door deze unieke kabels
                for c in cables:
                    distance_cable = house.distance(c)

                    # Als de afstand van de kabel beter is dan de beste afstand die geconstateerd is
                    if distance_cable < best_distance_cable:

                        # Zet dan deze kabel als de beste
                        best_distance_cable = distance_cable

                        # Onthoud de tuple/locatie van deze kabel
                        best_cable = c

            # Als de afstand van deze kabel dichterbijer ligt dan de afstand van de dichtsbijzijnste batterij
            if best_distance_cable < distance_battery:

                # Leg kabel vanuit huis naar deze dichtsbijzijndste kabel
                house.lay_cable_to_cable(best_cable, battery)

            # Anders sluit aan de dichtsbijzijnste batterij
            else:
                battery.lay_cable_to_house(house)

def diamond_dist_cap_cable(grid):
    """
        Algoritme die van buiten naar binnen batterijen aan dichtsbijzijnde huizen aansluit,
        die rekening houdt met dichtsbijzijnde kabels
    """
    segmenting_grid(grid)
    diamond_sorting_batteries(grid)
    diamond_bat_dist_cap(grid)
    diamond_lay_cables(grid)