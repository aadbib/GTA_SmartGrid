# Importeer libraries
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.offsetbox import TextArea, DrawingArea, AnnotationBbox, OffsetImage
import numpy as np
import csv
import sys
import os

# Zet root-pad goed om de modules vanaf CLI te laden
os.chdir(os.path.dirname(__file__))
root_path = os.path.dirname(os.getcwd())
sys.path.append(root_path)

# Importeer models
from models.Batterij import Batterij
from models.Huis import Huis

# Functie: tekent grid
def draw(wijk):
    # https://stackoverflow.com/questions/24943991/change-grid-interval-and-specify-tick-labels-in-matplotlib

    # Laadt alle objecten in de wijk
    objects = load_objects(wijk)

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
    photo_house = mpimg.imread('../images/huis_mini_mini.png')
    imagebox = OffsetImage(photo_house, zoom=1)
    addition_photo = AnnotationBbox(imagebox, (10, 30), frameon=False)
    ax.add_artist(addition_photo)
    plt.draw()
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

    # Roep draw aan
    draw(wijk)

if __name__=="__main__":
    main()