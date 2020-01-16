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
from algorithms.randomize_cable_dist_cap import rand_cable_dist_cap
from algorithms.randomize import rand_algorithm, rand_one_to_one_algorithm
from algorithms.worst_dist_no_capacity_restrictions import worst_dist
from algorithms.best_dist_no_capacity_restrictions import best_dist
from visualisation.plot_grid import draw

# Main functie
def main():

    # Moet argument wijk en pogingen meegeven
    if len(sys.argv) != 5:
        print("Usage: python main.py <wijk_nummer> <algoritme> <pogingen> <shared>")
        exit(1)

    wijk = str(sys.argv[1])

    # Argument moet 1, 2 of 3 zijn (wijken)
    if wijk not in ['1', '2', '3', '4']:
        print("No such wijk!")
        exit(1)

    sys_algorithm = sys.argv[2]

    if sys_algorithm not in ['1', '2', '3', '4', '5']:
        print("No such algorithm!")
        exit(1)

    try:
        pogingen = int(sys.argv[3])

    except:
        print("You have to give an integer")
        exit(1)

    shared_arg = sys.argv[4]
    if shared_arg not in ['0', '1']:
        print("Shared must be 0 or 1")
        exit(1)

    algorithms = {'1': rand_one_to_one_algorithm, '2': dist_cap_algorithm, '3': rand_cable_dist_cap, '4': worst_dist, '5': best_dist}
    algorithm = algorithms[sys_algorithm]

    """Algoritme kosten en run-time test, om de slechtste kosten en run-time in x pogingen te vinden"""

    Shared = True if shared_arg == '1' else False

    # Base-line worst-case, best-case
    slechtste_prijs = 0
    eind_beste_prijs = 1000000

    grid_beste = object

    print("Running algorithm, please wait...")
    start_time = time.time()
    for poging in range(pogingen):
        grid = Grid(wijk, f"{root_path}/data/wijk{wijk}_huizen.csv", f"{root_path}/data/wijk{wijk}_batterijen.csv")

        prijsbepaling = grid.get_unieke_total_prijs if Shared else grid.get_totale_prijs
        algorithm(grid)

        eind_prijs = prijsbepaling()

        if eind_prijs > slechtste_prijs:
            slechtste_prijs = eind_prijs

        if eind_prijs < eind_beste_prijs:
            eind_beste_prijs = eind_prijs
            grid_beste = grid

    print(f"Highest cost found: {slechtste_prijs}")
    print(f"Lowest cost found: {eind_beste_prijs}")
    print("--- %s seconds runtime ---" % (time.time() - start_time))

    draw(grid_beste)

if __name__=="__main__":
    main()