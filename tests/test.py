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
from algorithms.randomize import rand_one_to_one_algorithm
from algorithms.worst_dist import worst_dist_no_capacity_restrictions
from algorithms.best_dist import best_dist_no_capacity_restrictions, best_dist_no_cap_shared_cable
from visualisation.plot_grid import draw
from algorithms.bat_randomize_dist_cap import bat_dist_cap_algorithm

# Main functie
def main():

    # Moet argument wijk en pogingen meegeven
    if len(sys.argv) != 4:
        print("Usage: python main.py <wijk_nummer> <algoritme> <pogingen>")
        exit(1)

    neighbourhood = str(sys.argv[1])

    # Argument moet 1, 2 of 3 zijn (wijken)
    if neighbourhood not in ['1', '2', '3', '4']:
        print("No such neighbourhood!")
        exit(1)

    sys_algorithm = sys.argv[2]

    if sys_algorithm not in ['1', '2', '3', '4', '5', '6', '7']:
        print("No such algorithm!")
        exit(1)

    try:
        attempts = int(sys.argv[3])

    except:
        print("You have to give an integer")
        exit(1)

    algorithms = {
        '1': rand_one_to_one_algorithm,
        '2': dist_cap_algorithm,
        '3': rand_cable_dist_cap,
        '4': worst_dist_no_capacity_restrictions,
        '5': best_dist_no_capacity_restrictions,
        '6': best_dist_no_cap_shared_cable,
        '7': bat_dist_cap_algorithm
    }
    algorithm = algorithms[sys_algorithm]

    """Algoritme kosten en run-time test, om de slechtste kosten en run-time in x pogingen te vinden"""
    algorithms_shared_cable = {
        rand_one_to_one_algorithm: False,
        dist_cap_algorithm: False,
        rand_cable_dist_cap: True,
        worst_dist_no_capacity_restrictions: [True, False],
        best_dist_no_capacity_restrictions: False,
        best_dist_no_cap_shared_cable: True,
        bat_dist_cap_algorithm: False
    }

    if algorithm == worst_dist_no_capacity_restrictions:
        shared_question = input("Do you want to implement shared-cable strategy?\n Yes: [0]\n No: [1]\n")
        while shared_question not in ['0', '1']:
            shared_question = input("Try again: Do you want to implement shared-cable strategy?\n Yes: [0]\n No: [1]\n")
            if shared_question in ['0', '1']:
                break
        shared = algorithms_shared_cable[algorithm][int(shared_question)]

    else:
        shared = algorithms_shared_cable[algorithm]

    # Base-line worst-case, best-case
    worst_price = 0
    final_best_price = 1000000

    best_grid = None

    print("Running algorithm, please wait...")
    start_time = time.time()
    for attempt in range(attempts):
        grid = Grid(neighbourhood, f"{root_path}/data/wijk{neighbourhood}_huizen.csv", f"{root_path}/data/wijk{neighbourhood}_batterijen.csv")
        price_determination = grid.get_unique_total_price if shared else grid.get_total_price
        algorithm(grid)
        final_price = price_determination()

        if final_price > worst_price:
            worst_price = final_price

        if final_price < final_best_price:
            final_best_price = final_price
            best_grid = grid

    print(f"Highest cost found: {worst_price}")
    print(f"Lowest cost found: {final_best_price}")
    print("--- %s seconds runtime ---" % (time.time() - start_time))

    draw(best_grid)

if __name__=="__main__":
    main()