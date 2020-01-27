# Importeer libraries
from copy import deepcopy
from models.Segment import Segment

def segmenting_grid(grid):
    """
    Functie om segmenten uit een grid te maken
    Een segment bestaat uit 10 x 10
    Totaal segmenten: 25
    """

    starting_x = 0
    starting_y = 0

    batteries = deepcopy(grid.get_batteries())
    grid.clear_batteries()

    # Houd bij welke batterijen al geweest zijn
    deleted = []

    # Terwijl we nog niet het oppervlakte van een Grid hebben geraakt
    while starting_y < grid.ending_y:
        while starting_x < grid.ending_x:

            segment = Segment((starting_x, starting_y), (starting_x + Segment.x_size, starting_y + Segment.y_size))

            for battery in batteries:

                battery_location = battery.get_location()
                battery_x = int(battery_location[0])
                battery_y = int(battery_location[1])

                if (battery_x >= starting_x and battery_x <= (starting_x + Segment.x_size)) and (
                        battery_y >= starting_y and battery_y <= (starting_y + Segment.y_size)):

                    if battery not in deleted:
                        segment.set_battery(battery)
                        deleted.append(battery)

            grid.set_segment(segment)
            starting_x += Segment.x_size

        starting_x = 0
        starting_y += Segment.y_size

    deleted.clear()