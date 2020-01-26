# Importeer libraries
from copy import deepcopy
from functions.find import find_house
from functions.segmenting import segmenting_grid

class Diamond:
    """
    Diamond algoritme
    """

    @staticmethod
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


    @staticmethod
    def diamond_sorting_batteries(grid):
        """
        Algoritme die de batterijen sorteert, zodat batterijen op een diamante manier aangesloten worden
        """

        segment_order = [0, 20, 24, 4, 1, 5, 15, 21, 23, 19, 9, 3, 2, 6, 10, 16, 22, 18, 14, 8, 7, 11, 17, 13, 12]
        grid_segmenten = grid.get_segmenten()

        for order in segment_order:
            segment = grid_segmenten[order]

            # todo: CHECK OF is not None eruit kan
            if segment.get_battery() is not None:
                battery = segment.get_battery()
                grid.set_battery(battery)


    @staticmethod
    def diamond_lay_cables(grid):
        """
        Algoritme die ook naar bestaande gelegde kabels kijkt, en de de kabel/batterij kiest met minste afstand
        """

        batteries = grid.get_batteries()

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


    @staticmethod
    def diamond_dist_cap_cable(grid):
        """
            Algoritme die van buiten naar binnen batterijen aan dichtsbijzijnde huizen aansluit,
            die rekening houdt met dichtsbijzijnde kabels
        """

        segmenting_grid(grid)
        Diamond.diamond_sorting_batteries(grid)
        Diamond.diamond_bat_dist_cap(grid)
        Diamond.diamond_lay_cables(grid)