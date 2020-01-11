# Importeer libraries
import sys
import time

# Importeer grid, algoritme en visualisatie
from models.Grid import Grid
from algorithms.randomize_dist_cap import lay_cables
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
    lay_cables(grid)

    # Teken grid
    draw(grid)

    # Algoritme run-time test om de beste kosten en run-time in 10k pogingen te vinden
    # beste_prijs = 100000
    #
    # start_time = time.time()
    # for poging in range(10000):
    #     grid = Grid(wijk, f"data/wijk{wijk}_huizen.csv", f"data/wijk{wijk}_batterijen.csv")
    #     lay_cables(grid)
    #     eind_prijs = grid.get_totale_prijs()
    #     print(f'Totale prijs: {eind_prijs}')
    #
    #     if eind_prijs < beste_prijs:
    #         beste_prijs = eind_prijs
    #
    # print(beste_prijs)
    # print("--- %s seconds runtime ---" % (time.time() - start_time))

if __name__=="__main__":
    main()