# Importeer libraries
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.offsetbox import TextArea, DrawingArea, AnnotationBbox, OffsetImage
import numpy as np
import csv
import sys
import os

# Zet root-pad goed om de modules vanaf CLI te laden
os.chdir(os.path.dirname(os.path.abspath(__file__)))
root_path = os.path.dirname(os.getcwd())
sys.path.append(root_path)

# Importeer models
from models.Batterij import Batterij
from models.Huis import Huis

# Todo: Functie schrijven van afstand huis - batterij
# def distance(huis, batterij):


#Todo: vind optimale batterij, criteria: capaciteit & afstand
def find_battery(batterijen, huis):
    output_huis = huis.get_output()

    for batterij in batterijen:
        resterend = batterij.get_resterend()

        if resterend >= output_huis:
            return batterij


        # distance_y = int(batterij.get_locatie()[1]) - int(huis.get_locatie()[1])
        # distance_x = int(batterij.get_locatie()[0]) - int(huis.get_locatie()[0])



#Todo: Let op x en y van andere batterijen, no crossing
def lay_cable(huis, batterij):

    distance_y = int(batterij.get_locatie()[1]) - int(huis.get_locatie()[1])
    distance_x = int(batterij.get_locatie()[0]) - int(huis.get_locatie()[0])
    huis_y = int(huis.get_locatie()[1])
    huis_x = int(huis.get_locatie()[0])
    batterij_y = int(batterij.get_locatie()[1])

    if distance_y > 0:

        for movement in range(abs(distance_y)):
            huis.set_kabels((huis_x, huis_y + movement))
    else:

        for movement in range(abs(distance_y)):
            huis.set_kabels((huis_x, huis_y - movement))

    if distance_x > 0:

        for movement in range(abs(distance_x) + 1):
            huis.set_kabels((huis_x + movement, batterij_y))
    else:

        for movement in range(abs(distance_x) + 1):
            huis.set_kabels((huis_x - movement, batterij_y))


# Functie: tekent grid
def draw(wijk):
    # https://stackoverflow.com/questions/24943991/change-grid-interval-and-specify-tick-labels-in-matplotlib

    # Laadt alle objecten in de wijk
    objects = load_objects(wijk)

    # # Leg alle kabels tussen huizen en batterijen
    # lay_cables(objects)

    # Creer een figure en daarin een plot
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    # Arrays die de definitie van de lijnen vormen
    grote_lijnen = np.arange(0, 51, 10)
    kleine_lijnen = np.arange(0, 51, 1)

    # Zet deze arrays als x en y coordinaten
    ax.set_xticks(grote_lijnen)
    ax.set_xticks(kleine_lijnen, minor=True)
    ax.set_yticks(grote_lijnen)
    ax.set_yticks(kleine_lijnen, minor=True)

    # Maak een grid van deze multidimensional array
    ax.grid(which='major', alpha=10, linewidth=2)
    ax.grid(which='minor', alpha=1)

    # https://www.science-emergence.com/Articles/How-to-insert-an-image-a-picture-or-a-photo-in-a-matplotlib-figure/
    # https://gist.github.com/ppizarror/a36d214fd38a029cb80b7363bb133023
    # Fotos toevoegen
    for huis in objects['huizen']:
        huis_x = int(huis.get_locatie()[0])
        huis_y = int(huis.get_locatie()[1])

        photo_house = mpimg.imread('../images/huis_mini_mini.png')
        imagebox = OffsetImage(photo_house, zoom=1)
        addition_photo = AnnotationBbox(imagebox, (huis_x, huis_y), frameon=False)
        ax.add_artist(addition_photo)

    for batterij in objects['batterijen']:
        batterij_x = int(batterij.get_locatie()[0])
        batterij_y = int(batterij.get_locatie()[1])

        photo_battery = mpimg.imread('../images/batterij_mini_mini.png')
        imagebox2 = OffsetImage(photo_battery, zoom=1)
        addition_photo2 = AnnotationBbox(imagebox2, (batterij_x, batterij_y), frameon=False)
        ax.add_artist(addition_photo2)

    plt.savefig(f'{root_path}/images/add_picture_matplotlib_figure.png',bbox_inches='tight', transparent=True)

    # Toon de plot
    plt.show()

# Functie: Laadt alle objecten in wijk
def load_objects(wijk):

    objects = {"huizen": [], "batterijen": []}

    huizen_wijk = open(f'../data/wijk{wijk}_huizen.csv')
    batterijen_wijk = open(f'../data/wijk{wijk}_batterijen.csv')

    reader = csv.reader(huizen_wijk)

    # Skip eerste regel
    next(reader, None)

    # Loop door csv-reader, maak huis-objecten aan
    for x, y, output in reader:
        huis = Huis((x, y), output)
        objects["huizen"].append(huis)

    huizen_wijk.close()

    reader = csv.reader(batterijen_wijk)

    # Skip eerste regel
    next(reader, None)

    # Loop door csv-reader, maak batterij-objecten aan
    for positie, capaciteit in reader:
        batterij = Batterij(positie, capaciteit)
        objects["batterijen"].append(batterij)

    batterijen_wijk.close()

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

    objecten = load_objects(wijk)
    huizen = objecten["huizen"]

    for huis in huizen:
        batterij = find_battery(objecten["batterijen"], huis)
        lay_cable(huis, batterij)

    # Roep draw aan
    draw(wijk)

if __name__=="__main__":
    main()