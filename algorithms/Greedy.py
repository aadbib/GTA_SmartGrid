from functions.random import randomize_objects
from functions.find import find_battery, find_house

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