import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.lines as mlines
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
from models.Grid import Grid

# Zet root-pad goed om de modules vanaf CLI te laden
os.chdir(os.path.dirname(os.path.abspath(__file__)))
root_path = os.path.dirname(os.getcwd())
sys.path.append(root_path)

def draw(grid):
    """Functie die een weergave van een grid geeft"""

    # https://stackoverflow.com/questions/24943991/change-grid-interval-and-specify-tick-labels-in-matplotlib

    # Creëer een base-line figuur
    batteries = grid.get_batteries()
    fig = plt.figure()
    ax = fig.add_subplot(Grid.small_steps, Grid.small_steps, Grid.small_steps)

    # Arrays die de definitie van de lijnen vormen
    big_lines = np.arange(Grid.start_axis, Grid.end_axis, Grid.big_steps)
    small_lines = np.arange(Grid.start_axis, Grid.end_axis, Grid.small_steps)

    # Zet deze arrays als x en y coordinaten, tweede argument zorgt dat labels 0 ipv -1 wordt
    ax.set_xticks(big_lines, Grid.small_steps)
    ax.set_xticks(small_lines, minor=True)
    ax.set_yticks(big_lines, Grid.small_steps)
    ax.set_yticks(small_lines, minor=True)

    # Maak een grid van deze 2D array
    ax.grid(which='major', alpha=10, linewidth=2)
    ax.grid(which='minor', alpha=0)

    # https://www.science-emergence.com/Articles/How-to-insert-an-image-a-picture-or-a-photo-in-a-matplotlib-figure/
    # https://gist.github.com/ppizarror/a36d214fd38a029cb80b7363bb133023
    # Fotos toevoegen
    for battery_index, battery in enumerate(batteries):
        battery_x = int(battery.get_location()[0])
        battery_y = int(battery.get_location()[1])

        photo_battery = mpimg.imread(f'{root_path}/images/batterij_mini_mini.png')
        imagebox2 = OffsetImage(photo_battery, zoom=1)
        addition_photo2 = AnnotationBbox(imagebox2, (battery_x, battery_y), frameon=False)
        ax.add_artist(addition_photo2)
        houses = battery.get_houses()
        colors = ["cyan", "magenta", "green", "yellow", "red"]

        # Laadt locatie huizen en maak een image
        for house in houses:
            house_x = int(house.get_location()[0])
            house_y = int(house.get_location()[1])
            photo_house = mpimg.imread(f'{root_path}/images/huis_mini_mini.png')
            imagebox = OffsetImage(photo_house, zoom=1)
            addition_photo = AnnotationBbox(imagebox, (house_x, house_y), frameon=False)
            ax.add_artist(addition_photo)
            cables = house.get_cables()

            # Teken de kabels van de huizen met kleuren
            for index, cable in enumerate(cables):
                try:
                    # https://stackoverflow.com/questions/36470343/how-to-draw-a-line-with-matplotlib
                    # Werking:     x1, x2    y1, y2
                    #    x1, y1 = [20, 20], [21, 20]
                    #    x2, y2 = [22, 20], [21, 20]

                    cable1, cable2 = list(cable), list(cables[index + 1])
                    dashes = {"red":-0.1, "yellow":-0.05, "green":0, "cyan":0.05, "magenta":0.1}
                    x1, y1 = [
                                cable1[0] + dashes[colors[battery_index]],
                                cable2[0] + dashes[colors[battery_index]]
                             ],\
                             [
                                 cable1[1] + dashes[colors[battery_index]],
                                 cable2[1] + dashes[colors[battery_index]]
                             ]

                    line = ax.add_line(mlines.Line2D(x1, y1))
                    line.set_color(colors[battery_index])

                except IndexError:
                    pass
    plt.show()