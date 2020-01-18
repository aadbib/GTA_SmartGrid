from .randomize import randomize_objects

def find_worst_battery(batteries, house):
    """
    Zoekt de verste batterij voor een gegeven huis, waarbij de output niet uitmaakt
    """
    worst_index = 0
    max_distance = 0

    for index, battery in enumerate(batteries):
        try:
            distance_battery = house.distance(battery)

            if distance_battery > max_distance:
                worst_index = index
                max_distance = distance_battery

        except IndexError:
            pass

    return batteries[worst_index]


def worst_dist_no_capacity_restrictions(grid):
    """
    Algoritme die de slechtse batterij voor een huis linkt
    """
    houses = grid.get_houses()
    batteries = grid.get_batteries()
    for house in houses:
        battery = find_worst_battery(batteries, house)
        battery.lay_cable_to_house(house)


def worst_dist_no_cap_shared_cable(grid):
    """
    Algoritme die ook naar bestaande gelegde kabels kijkt, en de de kabel/batterij kiest met minste afstand
    """
    houses = grid.get_houses()
    batteries = grid.get_batteries()

    randomize_objects(houses, batteries)

    # Voor huis in huizen
    for house in houses:

        # Zoek de slechtste batterij
        battery = find_worst_battery(batteries, house)

        # Bereken de afstand tussen de slechtste batterij en huis
        distance_battery = house.distance(battery)

        # Base-line afstand kabel (Upper-bound)
        worst_distance_cable = 0

        # Declaratie slechtste kabel
        worst_cable = tuple

        # Loop door de batterijen array
        for b in batteries:

            # Pak de unieke kabels die aan de batterij is aangesloten
            cables = b.get_unique_cables()

            # Loop door deze unieke kabels
            for c in cables:
                distance_cable = house.distance(c)

                # Als de afstand van de kabel meer is dan de slechtste afstand die geconstateerd is
                if distance_cable > worst_distance_cable:

                    # Zet dan dan deze kabel als de slechtste
                    worst_distance_cable = distance_cable

                    # Onthoud de tuple/locatie van deze kabel
                    worst_cable = c

                    # Onthoud van welke batterij deze kabel komt
                    battery_cable = b

        # Als de afstand van deze kabel verder ligt dan de afstand van de verste batterij
        if worst_distance_cable > distance_battery:
            battery_cable.set_house(house)

            # Leg kabel vanuit huis naar deze verste kabel
            house.lay_cable_to_cable(worst_cable, battery_cable)

        # Anders sluit aan de verste batterij
        else:
            battery.lay_cable_to_house(house)