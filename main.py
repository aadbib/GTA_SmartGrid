# Importeer libraries
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.lines as mlines
from matplotlib.offsetbox import TextArea, DrawingArea, AnnotationBbox, OffsetImage
import numpy as np
import csv
import sys

# Importeer models
from models.Batterij import Batterij
from models.Huis import Huis

def totale_prijs(batterijen):
    eind_prijs = 0

    for batterij in batterijen:
        eind_prijs += batterij.total_price()

    return eind_prijs

# Functie: tekent grid
def draw(wijk):
    # https://stackoverflow.com/questions/24943991/change-grid-interval-and-specify-tick-labels-in-matplotlib

    # Laadt alle objecten in de wijk
    objects = load_objects(wijk)

    # Stop batterijen in variabele
    batterijen = objects["batterijen"]

    eind_prijs = totale_prijs(batterijen)

    print(f'Totale prijs: {eind_prijs}')

    # Creëer een figure en daarin een plot
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    # Arrays die de definitie van de lijnen vormen
    grote_lijnen = np.arange(-1, 52, 10)
    kleine_lijnen = np.arange(-1, 52, 1)

    # Zet deze arrays als x en y coordinaten, tweede argument zorgt dat labels 0 ipv -1
    ax.set_xticks(grote_lijnen, 1)
    ax.set_xticks(kleine_lijnen, minor=True)
    ax.set_yticks(grote_lijnen, 1)
    ax.set_yticks(kleine_lijnen, minor=True)

    # Maak een grid van deze multidimensional array
    # Alpha is alleen transparency
    # Todo: zoek uit hoe je die negatieve 2d grid kan aanpassen, zodat die y-as bij 0 begint, en titels goed zijn
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

        print(f"Batterij: {batterij.get_resterend()}")

        for huis in huizen:
            huis_x = int(huis.get_locatie()[0])
            huis_y = int(huis.get_locatie()[1])

            photo_house = mpimg.imread('images/huis_mini_mini.png')
            imagebox = OffsetImage(photo_house, zoom=1)
            addition_photo = AnnotationBbox(imagebox, (huis_x, huis_y), frameon=False)
            ax.add_artist(addition_photo)

            print(f"Huis: {huis.get_output()}")

            kabels = huis.get_kabels()
            for index, kabel in enumerate(kabels):
                try:
                    # https://stackoverflow.com/questions/36470343/how-to-draw-a-line-with-matplotlib
                    #           x1, x2    y1, y2
                    # x1, y1 = [20, 20], [21, 20]
                    # x2, y2 = [22, 20], [21, 20]

                    kabel1, kabel2 = list(kabel), list(kabels[index + 1])
                    dashes = {"red":-0.1, "yellow":-0.05, "green":0, "cyan":0.05, "magenta":0.1}
                    x1, y1 = [kabel1[0] + dashes[kleuren[batterij_index]], kabel2[0] + dashes[kleuren[batterij_index]] ], [kabel1[1] + dashes[kleuren[batterij_index]], kabel2[1] + dashes[kleuren[batterij_index]]]

                    line = ax.add_line(mlines.Line2D(x1, y1))

                    line.set_color(kleuren[batterij_index])

                    # line.set_dashes(dashes[kleuren[batterij_index]])

                except IndexError:
                    pass

    plt.savefig('images/add_picture_matplotlib_figure.png',bbox_inches='tight', transparent=True)

    # Toon de plot
    plt.show()

# Functie: Laadt alle objecten in wijk
def load_objects(wijk):

    objects = {"huizen": [], "batterijen": []}

    huizen_wijk = open(f'data/wijk{wijk}_huizen.csv')
    batterijen_wijk = open(f'data/wijk{wijk}_batterijen.csv')

    # DictReader
    reader = csv.DictReader(huizen_wijk)

    # Loop door csv-reader, maak huis-objecten aan
    for line in reader:
        huis = Huis((line['x'], line[' y']), line[' max output'])
        objects["huizen"].append(huis)

    huizen_wijk.close()
    reader = csv.DictReader(batterijen_wijk)

    # Loop door csv-reader, maak batterij-objecten aan
    for line in reader:
        batterij = Batterij(line['positie'], line[' capaciteit'])
        objects["batterijen"].append(batterij)

    batterijen_wijk.close()

    # Stop huizen en batterijen in variabelen
    huizen = objects["huizen"]
    batterijen = objects["batterijen"]

    # Leg alle kabels tussen huizen en batterijen
    for huis in huizen:
        batterij = huis.find_battery(batterijen)
        batterij.lay_cable(huis)

    return objects

# Main functie
def main():

    # Moet argument wijk meegeven
    if len(sys.argv) != 2:
        print("Usage: python main.py <wijk_nummer>")
        exit(1)

    wijk = str(sys.argv[1])

    # Argument moet 1, 2 of 3 zijn (wijken)
    if wijk not in ['1', '2', '3']:
        print("No such wijk!")
        exit(1)

    # Roep draw aan
    draw(wijk)

if __name__=="__main__":
    main()