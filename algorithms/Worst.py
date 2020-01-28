from functions.random import randomize_objects
from functions.find import find_worst_battery

class Worst:
    """Slechtste scenario algoritme"""

    @staticmethod
    def worst_dist_no_capacity_restrictions(grid):
        """Algoritme die de slechtse batterij voor een huis linkt"""

        houses = grid.get_houses()
        batteries = grid.get_batteries()
        for house in houses:
            battery = find_worst_battery(batteries, house)
            battery.lay_cable_to_house(house)

    @staticmethod
    def worst_dist_no_cap_shared_cable(grid):
        """
            Algoritme die ook naar bestaande gelegde kabels kijkt,
            en de de kabel/batterij kiest met minste afstand
        """

        # Verkrijg batterijen en huizen en schud ze
        houses = grid.get_houses()
        batteries = grid.get_batteries()
        randomize_objects(houses, batteries)

        for house in houses:

            # Zoek de slechtste batterij, bereken afstand met huis en houd gegevens bij
            battery = find_worst_battery(batteries, house)
            distance_battery = house.distance(battery)
            worst_distance_cable = 0
            worst_cable = tuple

            for b in batteries:
                cables = b.get_unique_cables()

                for c in cables:
                    distance_cable = house.distance(c)

                    # Als het kan, wijzig slechtste kabel en afstand en onthoud gegevens
                    if distance_cable > worst_distance_cable:
                        worst_distance_cable = distance_cable
                        worst_cable = c
                        battery_cable = b

            # Conditie: controleer afstand batterij en kabel, en selecteert minste afstand
            if worst_distance_cable > distance_battery:
                battery_cable.set_house(house)
                house.lay_cable_to_cable(worst_cable, battery_cable)

            else:
                battery.lay_cable_to_house(house)