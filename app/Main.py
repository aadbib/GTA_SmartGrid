# Importeer libraries
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.offsetbox import TextArea, DrawingArea, AnnotationBbox, OffsetImage
import numpy as np
import csv
from models.Batterij import Batterij
from models.Huis import Huis


# Functie die de grid gaat tekenen
def draw():
    # https://stackoverflow.com/questions/24943991/change-grid-interval-and-specify-tick-labels-in-matplotlib

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
    plt.savefig('add_picture_matplotlib_figure.png',bbox_inches='tight', transparent=True)

    # Toon de plot
    plt.show()

def load_objects(wijk):

    if wijk not in ['1', '2', '3']:
        return "No such wijk!"

    objects = {"huizen": [], "batterijen": []}

    huizen_wijk = open(f'../data/wijk{wijk}_huizen.csv')
    batterijen_wijk = open(f'../data/wijk{wijk}_batterijen.csv')

    reader = csv.reader(huizen_wijk)

    # Skip eerste regel
    next(reader, None)

    for x, y, output in reader:
        huis = Huis((x, y), output)
        objects["huizen"].append(huis)

    huizen_wijk.close()

    reader = csv.reader(batterijen_wijk)

    # Skip eerste regel
    next(reader, None)

    for positie, capaciteit in reader:
        batterij = Batterij(positie, capaciteit)
        objects["batterijen"].append(batterij)

    batterijen_wijk.close()

    return objects

# main functie
def main():
    wijk = str(input("Welke wijk wil je inladen?"))
    objects = load_objects(wijk)
    draw()



if __name__=="__main__":
    main()