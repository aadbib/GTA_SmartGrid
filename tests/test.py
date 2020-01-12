# Importeer libraries
import sys
import os
import time

# Zet root-pad goed om de modules vanaf CLI te laden
os.chdir(os.path.dirname(os.path.abspath(__file__)))
root_path = os.path.dirname(os.getcwd())
sys.path.append(root_path)

# Importeer grid, algoritmes en visualisatie
from models.Grid import Grid
from algorithms.randomize_dist_cap import dist_cap_algorithm
from algorithms.randomize import rand_algorithm, rand_one_to_one_algorithm

# Main functie
def main():

    # Moet argument wijk en pogingen meegeven
    if len(sys.argv) != 4:
        print("Usage: python main.py <wijk_nummer> <algoritme> <pogingen>")
        exit(1)

    wijk = str(sys.argv[1])

    # Argument moet 1, 2 of 3 zijn (wijken)
    if wijk not in ['1', '2', '3']:
        print("No such wijk!")
        exit(1)

    sys_algorithm = sys.argv[2]

    if sys_algorithm not in ['1', '2', '3']:
        print("No such algorithm!")
        exit(1)

    try:
        pogingen = int(sys.argv[3])

    except:
        print("You have to give an integer")
        exit(1)

    algorithms = {'1': dist_cap_algorithm, '2': rand_one_to_one_algorithm, '3': rand_algorithm}
    algorithm = algorithms[sys_algorithm]

    """Algoritme kosten en run-time test, om de slechtste kosten en run-time in x pogingen te vinden"""

    # Base-line worst-case, best-case
    slechtste_prijs = 0
    beste_prijs = 1000000

    print("Running algorithm, please wait...")
    start_time = time.time()
    for poging in range(pogingen):
        grid = Grid(wijk, f"{root_path}/data/wijk{wijk}_huizen.csv", f"{root_path}/data/wijk{wijk}_batterijen.csv")
        algorithm(grid)
        eind_prijs = grid.get_totale_prijs()

        if eind_prijs > slechtste_prijs:
            slechtste_prijs = eind_prijs

        if eind_prijs < beste_prijs:
            beste_prijs = eind_prijs

    print(f"Highest cost found: {slechtste_prijs}")
    print(f"Lowest cost found: {beste_prijs}")
    print("--- %s seconds runtime ---" % (time.time() - start_time))

if __name__=="__main__":
    main()