# Importeer libraries
import matplotlib.pyplot as plt
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

    # Toon de plot
    plt.show()

# main functie
def main():
    draw()

if __name__=="__main__":
    main()