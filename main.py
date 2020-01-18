# Importeer libraries
import sys

# Importeer grid, algoritmes en visualisatie
# Importeer grid, algoritmes en visualisatie
from models.Grid import Grid
from algorithms.randomize_dist_cap import dist_cap_algorithm
from algorithms.randomize_cable_dist_cap import rand_cable_dist_cap
from algorithms.randomize import rand_one_to_one_algorithm
from algorithms.worst_dist import worst_dist_no_capacity_restrictions
from algorithms.best_dist import best_dist_no_capacity_restrictions, best_dist_no_cap_shared_cable
from visualisation.plot_grid import draw
import os
import sys

# Zet root-pad goed om de modules vanaf CLI te laden
os.chdir(os.path.dirname(os.path.abspath(__file__)))
root_path = os.path.dirname(os.getcwd())
sys.path.append(root_path)

# Main functie
def main():

    # Moet argument wijk meegeven
    if len(sys.argv) != 3:
        print("Usage: python main.py <wijk_nummer> <algoritme>")
        exit(1)

    neighbourhood = str(sys.argv[1])

    # Argument moet 1, 2 of 3 zijn (wijken)
    if neighbourhood not in ['1', '2', '3']:
        print("No such neighbourhood!")
        exit(1)

    sys_algorithm = sys.argv[2]

    if sys_algorithm not in ['1', '2', '3']:
        print("No such algorithm!")
        exit(1)

    algorithms = {'1': dist_cap_algorithm, '2': rand_one_to_one_algorithm}
    algorithm = algorithms[sys_algorithm]

    grid = Grid(neighbourhood, f"{root_path}/data/wijk{neighbourhood}_huizen.csv", f"{root_path}/data/wijk{neighbourhood}_batterijen.csv")

    # Voer algoritme op grid uit
    algorithm(grid)

    # Teken grid
    draw(grid)

if __name__=="__main__":
    main()