from functions.random import randomize_objects
from functions.find import find_best_battery

class Best:
    """Algoritmen die theoretische lowerbound voorstellen"""

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


