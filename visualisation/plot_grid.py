# Importeer libraries
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.lines as mlines
from matplotlib.offsetbox import TextArea, DrawingArea, AnnotationBbox, OffsetImage
import numpy as np
from models.Grid import Grid

# Functie: tekent grid
def draw(grid):
    # https://stackoverflow.com/questions/24943991/change-grid-interval-and-specify-tick-labels-in-matplotlib

    # Stop batterijen in variabele
    batterijen = grid.get_batterijen()

    # Creëer een figure en daarin een plot
    fig = plt.figure()
    ax = fig.add_subplot(Grid.kleine_stappen, Grid.kleine_stappen, Grid.kleine_stappen)

    # Arrays die de definitie van de lijnen vormen
    grote_lijnen = np.arange(Grid.begin_as, Grid.eind_as, Grid.grote_stappen)
    kleine_lijnen = np.arange(Grid.begin_as, Grid.eind_as, Grid.kleine_stappen)

    # Zet deze arrays als x en y coordinaten, tweede argument zorgt dat labels 0 ipv -1 wordt
    ax.set_xticks(grote_lijnen, Grid.kleine_stappen)
    ax.set_xticks(kleine_lijnen, minor=True)
    ax.set_yticks(grote_lijnen, Grid.kleine_stappen)
    ax.set_yticks(kleine_lijnen, minor=True)

    # Maak een grid van deze multidimensional array
    # Alpha is alleen transparency
    ax.grid(which='major', alpha=10, linewidth=2)
    ax.grid(which='minor', alpha=1)

    # https://www.science-emergence.com/Articles/How-to-insert-an-image-a-picture-or-a-photo-in-a-matplotlib-figure/
    # https://gist.github.com/ppizarror/a36d214fd38a029cb80b7363bb133023
    # Fotos toevoegen
    for batterij_index, batterij in enumerate(batterijen):
        batterij_x = int(batterij.get_locatie()[0])
        batterij_y = int(batterij.get_locatie()[1])

        photo_battery = mpimg.imread('images/batterij_mini_mini.png')
        imagebox2 = OffsetImage(photo_battery, zoom=1)
        addition_photo2 = AnnotationBbox(imagebox2, (batterij_x, batterij_y), frameon=False)
        ax.add_artist(addition_photo2)

        huizen = batterij.get_huizen()
        kleuren = ["cyan", "magenta", "green", "yellow", "red"]

        for huis in huizen:
            huis_x = int(huis.get_locatie()[0])
            huis_y = int(huis.get_locatie()[1])

            photo_house = mpimg.imread('images/huis_mini_mini.png')
            imagebox = OffsetImage(photo_house, zoom=1)
            addition_photo = AnnotationBbox(imagebox, (huis_x, huis_y), frameon=False)
            ax.add_artist(addition_photo)

            kabels = huis.get_kabels()
            for index, kabel in enumerate(kabels):
                try:
                    # https://stackoverflow.com/questions/36470343/how-to-draw-a-line-with-matplotlib
                    #           x1, x2    y1, y2
                    # x1, y1 = [20, 20], [21, 20]
                    # x2, y2 = [22, 20], [21, 20]

                    kabel1, kabel2 = list(kabel), list(kabels[index + 1])
                    dashes = {"red":-0.1, "yellow":-0.05, "green":0, "cyan":0.05, "magenta":0.1}
                    x1, y1 = [
                                kabel1[0] + dashes[kleuren[batterij_index]],
                                kabel2[0] + dashes[kleuren[batterij_index]]
                             ],\
                             [
                                 kabel1[1] + dashes[kleuren[batterij_index]],
                                 kabel2[1] + dashes[kleuren[batterij_index]]
                             ]

                    line = ax.add_line(mlines.Line2D(x1, y1))
                    line.set_color(kleuren[batterij_index])

                except IndexError:
                    pass

    plt.savefig('images/add_picture_matplotlib_figure.png',bbox_inches='tight', transparent=True)

    # Toon de plot
    plt.show()