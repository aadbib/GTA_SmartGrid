# Importeer libraries
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.offsetbox import TextArea, DrawingArea, AnnotationBbox, OffsetImage
import numpy as np

# Functie die de grid gaat tekenen
def draw():

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

# main functie
def main():
    draw()

if __name__=="__main__":
    main()