# Importeer libraries
from functions.random import randomize_objects
from functions.find import find_battery, find_best_battery, find_house
from copy import deepcopy

class Greedy:
    "Greedy algoritmen"

    @staticmethod
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


    @staticmethod
    def best_dist_no_capacity_restrictions(grid):
        """
        Algoritme die de slechtse batterij voor een huis linkt
        """
        houses = grid.get_houses()
        batteries = grid.get_batteries()
        for house in houses:
            battery = find_best_battery(batteries, house)
            battery.lay_cable_to_house(house)


    @staticmethod
    def best_dist_no_cap_shared_cable(grid):
        """
        Algoritme die ook naar bestaande gelegde kabels kijkt, en de de kabel/batterij kiest met minste afstand
        """
        houses = grid.get_houses()
        batteries = grid.get_batteries()

        randomize_objects(houses, batteries)

        # Voor huis in huizen
        for house in houses:

            # Zoek de dichtsbijzijndste batterij
            battery = find_best_battery(batteries, house)

            # Bereken de afstand tussen de beste batterij en huis
            distance_battery = house.distance(battery)

            # Base-line afstand kabel (Upper-bound)
            best_distance_cable = 1000000

            # Declaratie beste kabel
            best_cable = tuple

            # Loop door de batterijen array
            for b in batteries:

                # Pak de unieke kabels die aan de batterij is aangesloten
                cables = b.get_unique_cables()

                # Loop door deze unieke kabels
                for c in cables:
                    distance_cable = house.distance(c)

                    # Als de afstand van de kabel beter is dan de beste afstand die geconstateerd is
                    if distance_cable < best_distance_cable:
                        # Zet dan dan deze kabel als de beste
                        best_distance_cable = distance_cable

                        # Onthoud de tuple/locatie van deze kabel
                        best_cable = c

                        # Onthoud van welke batterij deze kabel komt
                        battery_cable = b

            # Als de afstand van deze kabel dichterbijer ligt dan de afstand van de dichtsbijzijnste batterij
            if best_distance_cable < distance_battery:
                battery_cable.set_house(house)

                # Leg kabel vanuit huis naar deze dichtsbijzijndste kabel
                house.lay_cable_to_cable(best_cable, battery_cable)

            # Anders sluit aan de dichtsbijzijnste batterij
            else:
                battery.lay_cable_to_house(house)


    @staticmethod
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


    @staticmethod
    def rand_cable_dist_cap(grid):
        """
        Algoritme die ook naar bestaande gelegde kabels kijkt, en de de kabel/batterij kiest met minste afstand
        """
        houses = grid.get_houses()
        batteries = grid.get_batteries()

        randomize_objects(houses, batteries)

        # Voor huis in huizen
        for house in houses:

            # Zoek de dichtsbijzijndste batterij
            battery = find_battery(batteries, house)

            # Bereken de afstand tussen de beste batterij en huis
            distance_battery = house.distance(battery)

            # Base-line afstand kabel (Upper-bound)
            best_distance_cable = 1000000

            # Declaratie beste kabel
            best_cable = tuple

            # Loop door de batterijen array
            for b in batteries:

                # Pak de resterende capaciteit van elke batterij
                remaining = b.get_remaining()

                # Als de batterij uberhaupt verbindingen heeft, anders prune
                if not b.is_empty():

                    # Als de batterij capaciteit nog voldoet, anders prune
                    if remaining >= house.get_output():

                        # Pak de unieke kabels die aan de batterij is aangesloten
                        cables = b.get_unique_cables()

                        # Loop door deze unieke kabels
                        for c in cables:
                            distance_cable = house.distance(c)

                            # Als de afstand van de kabel beter is dan de beste afstand die geconstateerd is
                            if distance_cable < best_distance_cable:

                                # Zet dan deze kabel als de beste
                                best_distance_cable = distance_cable

                                # Onthoud de tuple/locatie van deze kabel
                                best_cable = c

                                # Onthoud van welke batterij deze kabel komt
                                battery_cable = b

            # Als de afstand van deze kabel dichterbijer ligt dan de afstand van de dichtsbijzijnste batterij
            if best_distance_cable < distance_battery:
                battery_cable.set_house(house)

                # Leg kabel vanuit huis naar deze dichtsbijzijndste kabel
                house.lay_cable_to_cable(best_cable, battery_cable)

            # Anders sluit aan de dichtsbijzijnste batterij
            else:
                battery.lay_cable_to_house(house)