from copy import deepcopy
from functions.find import find_house
from functions.segmenting import segmenting_grid
from functions.fit import fit_house_in_diamond

class Diamond:
    """Diamond algoritme"""

    @staticmethod
    def diamond_bat_dist_cap(grid):
        """
            Algoritme die 'random' de batterijen aan de zo dichtbijzijnste huizen aansluit,
            waarbij de output in de capaciteit past
        """

        houses = grid.get_houses()
        batteries = grid.get_batteries()
        houses_copy = deepcopy(houses)

        for battery in batteries:

            # Batterij blijft huizen toevoegen tot find_house niks returned, oftewel batterij vol
            while True:
                house = find_house(battery, houses_copy)

                if house:
                    battery.set_house(house)

                else:
                    break

        # Als er nog een huis over is, los dit op
        if len(houses_copy) >= 1:
            fit_house_in_diamond(houses_copy, batteries)


    @staticmethod
    def diamond_sorting_batteries(grid):
        """
            Algoritme die de batterijen sorteert,
            zodat batterijen op een diamante manier aangesloten worden
        """

        # Bepaal volgorde diamant
        segment_order = [0, 20, 24, 4, 1, 5, 15, 21, 23, 19, 9, 3, 2, 6, 10, 16, 22, 18, 14, 8, 7, 11, 17, 13, 12]
        grid_segmenten = grid.get_segmenten()

        for order in segment_order:
            segment = grid_segmenten[order]

            if segment.get_battery():
                battery = segment.get_battery()
                grid.set_battery(battery)


    @staticmethod
    def diamond_lay_cables(grid):
        """
            Algoritme die ook naar bestaande gelegde kabels kijkt,
            en de de kabel/batterij kiest met minste afstand
        """

        batteries = grid.get_batteries()

        for battery in batteries:
            houses = battery.get_houses()

            for house in houses:

                distance_battery = house.distance(battery)
                best_distance_cable = 1000000
                best_cable = tuple

                # Als de batterij uberhaupt verbindingen heeft, pak kabels, anders prune
                if not battery.is_empty():
                    cables = battery.get_unique_cables()

                    for c in cables:
                        distance_cable = house.distance(c)

                        # Als het kan, wijzig beste kabel en afstand
                        if distance_cable < best_distance_cable:
                            best_distance_cable = distance_cable
                            best_cable = c

                # Conditie: controleer afstand batterij en kabel, en selecteert minste afstand
                if best_distance_cable < distance_battery:
                    house.lay_cable_to_cable(best_cable, battery)

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