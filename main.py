# Importeer libraries
import sys

# Importeer grid, algoritmes en visualisatie
from models.Grid import Grid
from algorithms.randomize_dist_cap import dist_cap_algorithm
from algorithms.randomize import rand_algorithm, rand_one_to_one_algorithm
from visualisation.plot_grid import draw

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

    grid = Grid(wijk, f"data/wijk{wijk}_huizen.csv", f"data/wijk{wijk}_batterijen.csv")

    # Voer algoritme op grid uit
    dist_cap_algorithm(grid)

    # Teken grid
    draw(grid)

if __name__=="__main__":
    main()