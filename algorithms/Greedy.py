# Importeer libraries
from functions.random import randomize_objects
from functions.find import find_battery, find_best_battery, find_house
from copy import deepcopy

class Greedy:
    "Greedy algoritmen"

    @staticmethod
    def dist_cap_algorithm(grid):
        """
            Algoritme die 'random' de huizen aan de zo dichtbijzijnste batterij aansluit,
            waarbij de output in de capaciteit past
        """

        houses = grid.get_houses()
        batteries = grid.get_batteries()

        randomize_objects(houses, batteries)

        for house in houses:
            battery = find_battery(batteries, house)
            battery.lay_cable_to_house(house)


    @staticmethod
    def best_dist_no_capacity_restrictions(grid):
        """Algoritme die de slechtse batterij voor een huis linkt"""

        houses = grid.get_houses()
        batteries = grid.get_batteries()
        for house in houses:
            battery = find_best_battery(batteries, house)
            battery.lay_cable_to_house(house)


    @staticmethod
    def best_dist_no_cap_shared_cable(grid):
        """
            Algoritme die ook naar bestaande gelegde kabels kijkt,
            en de de kabel/batterij kiest met minste afstand
        """

        houses = grid.get_houses()
        batteries = grid.get_batteries()
        randomize_objects(houses, batteries)

        for house in houses:

            # Initialiseer variabelen voor bepaling batterij gegevens
            battery = find_best_battery(batteries, house)
            distance_battery = house.distance(battery)
            best_distance_cable = 1000000
            best_cable = tuple

            for b in batteries:

                cables = b.get_unique_cables()
                for c in cables:
                    distance_cable = house.distance(c)

                    # Als de afstand van de kabel beter is dan de beste afstand die geconstateerd is
                    if distance_cable < best_distance_cable:
                        best_distance_cable = distance_cable
                        best_cable = c
                        battery_cable = b

            # Controleer afstand kabel met dichtsbijzijnste batterij, beter: sluit aan
            if best_distance_cable < distance_battery:
                battery_cable.set_house(house)
                house.lay_cable_to_cable(best_cable, battery_cable)

            # Anders: sluit aan dichtsbijzijnste batterij
            else:
                battery.lay_cable_to_house(house)


    @staticmethod
    def bat_dist_cap_algorithm(grid):
        """
            Algoritme die 'random' de batterijen aan de zo dichtbijzijnste huizen aansluit,
            waarbij de output in de capaciteit past
        """

        # Verkrijg huizen en batterijen, schud ze, en pak kopie van huizen
        houses = grid.get_houses()
        batteries = grid.get_batteries()
        randomize_objects(houses, batteries)
        houses_copy = deepcopy(houses)

        for battery in batteries:

            # Batterij blijft huizen toevoegen tot find_house niks returned, oftewel batterij vol
            while True:
                house = find_house(battery, houses_copy)

                if house:
                    battery.lay_cable_to_house(house)

                else:
                    break


    @staticmethod
    def rand_cable_dist_cap(grid):
        """
            Algoritme die ook naar bestaande gelegde kabels kijkt,
            en de de kabel/batterij kiest met minste afstand
        """

        # Verkrijg huizen en batterijen en schud ze
        houses = grid.get_houses()
        batteries = grid.get_batteries()
        randomize_objects(houses, batteries)

        for house in houses:

            # Zoek dichtsbijzijndste batterij, bepaal afstand, en houd bij met afstand kabel
            battery = find_battery(batteries, house)
            distance_battery = house.distance(battery)
            best_distance_cable = 1000000
            best_cable = tuple

            for b in batteries:

                # Pak resterende capaciteit batterij
                remaining = b.get_remaining()

                # Condities op kabels en output, prune als niet voldoet
                if not b.is_empty():
                    if remaining >= house.get_output():
                        cables = b.get_unique_cables()

                        for c in cables:
                            distance_cable = house.distance(c)

                            # Is er een kabel dichterbijer, sla dit op en onthoud gegevens
                            if distance_cable < best_distance_cable:
                                best_distance_cable = distance_cable
                                best_cable = c
                                battery_cable = b

            # Conditie: controleer afstand batterij en kabel, en selecteert minste afstand
            if best_distance_cable < distance_battery:
                battery_cable.set_house(house)
                house.lay_cable_to_cable(best_cable, battery_cable)

            else:
                battery.lay_cable_to_house(house)