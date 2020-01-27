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

    # # Fixen van huizen die niet bij een batterij passen
    # print(len(houses_copy))            
    # print(houses_copy[0])

    # Als er nog een huis over is, los dit op
    if len(houses_copy) >= 1:
        capacity_missing_house = houses_copy[0].get_output()
        index_battery = None
        battery_with_most_capacity = 0

        # Pak de batterij met de meeste resterende capaciteit
        for index, battery in enumerate(batteries):
            remaining_battery = battery.get_remaining()

            if battery_with_most_capacity < remaining_battery:
                battery_with_most_capacity = remaining_battery
                index_battery = index
        
        # Kijk naar de huizen in de eerst batterij
        houses_first_battery = batteries[index_battery].get_houses()
        index_house = None 
        house_most_output = 0
        
        # Pak het huis met de hoogste output
        for index, house in enumerate(houses_first_battery):
            output_house = house.get_output()

            if house_most_output < output_house:
                house_most_output = output_house
                index_house = index

        second_battery_index = None
        second_most_battery_capacity = 0

        # Pak de batterij met daarna de meeste resterende capaciteit
        for index, battery in enumerate(batteries):
            remaining_battery = battery.get_remaining()
            
            if second_most_battery_capacity < remaining_battery and index_battery is not index:
                second_most_battery_capacity = remaining_battery
                second_battery_index = index

        # Kijk naar de huizen in de tweede batterij
        houses_second_battery = batteries[second_battery_index].get_houses()
        second_index_house = None 
        second_house_output = 100
        
        # Pak het huis met een output dat ervoor zorgt dat missende huis past
        for index, house in enumerate(houses_second_battery):
            output_house = house.get_output()

            # Let hierop dat de eerste en tweede batterij de wissel aankunnen en dat er in één wissel genoeg ruimte is voor het missende huis
            if (house_most_output - output_house) < second_most_battery_capacity and (battery_with_most_capacity + (house_most_output - output_house)) > capacity_missing_house:
                second_house_output = output_house
                second_index_house = index
                break

        # # Als er geen passend huis wordt, gevonden los dit op 
        # if second_index_house is None:
        #     pass

        

        print(house_most_output)
        print(second_house_output)
        print(houses_copy[0])
        # swap houses AKA pop them both from their respected batteries and add them
        # check output
        # if the final house still doesnt fit in the battery with most capacity, do process again
        # else there is your final grid        

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