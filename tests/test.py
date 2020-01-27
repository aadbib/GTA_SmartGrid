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
from algorithms.Random import Random
from algorithms.Greedy import Greedy
from algorithms.Worst import Worst
from algorithms.Diamond import Diamond
from algorithms.Hillclimber import Hillclimber
from visualisation.plot_grid import draw


# Variabele die functie-referenties van de algoritmen opslaan
random_algorithm = Random.rand_one_to_one_algorithm
greedy_no_shared = Greedy.dist_cap_algorithm
greedy_shared = Greedy.rand_cable_dist_cap
greedy_no_shared_restrict_off = Greedy.best_dist_no_capacity_restrictions
greedy_shared_restrict_off = Greedy.best_dist_no_cap_shared_cable
greedy_bat_no_shared = Greedy.bat_dist_cap_algorithm
worst_algorithm = Worst.worst_dist_no_capacity_restrictions
diamond_algorithm = Diamond.diamond_dist_cap_cable
hill_climber = Hillclimber.hill_climber_algorithm


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

    if sys_algorithm not in ['1', '2', '3', '4', '5', '6', '7', '8']:
        print("No such algorithm!")
        exit(1)

    try:
        attempts = int(sys.argv[3])

    except:
        print("You have to give an integer")
        exit(1)

    algorithms = {
        '1': random_algorithm,
        '2': greedy_no_shared,
        '3': greedy_shared,
        '4': worst_algorithm,
        '5': greedy_no_shared_restrict_off,
        '6': greedy_shared_restrict_off,
        '7': greedy_bat_no_shared,
        '8': diamond_algorithm
    }
    algorithm = algorithms[sys_algorithm]

    algorithms_shared_cable = {
        random_algorithm: False,
        greedy_no_shared: False,
        greedy_shared: True,
        worst_algorithm: [True, False],
        greedy_no_shared_restrict_off: False,
        greedy_shared_restrict_off: True,
        greedy_bat_no_shared: False,
        diamond_algorithm: True
    }

    # Worst algoritme kan zowel met als zonder gedeelde kabels, dus vraag welke
    if algorithm == worst_algorithm:
        shared_question = input("Do you want to implement shared-cable strategy?\nYes: [0]\nNo: [1]\n")
        while shared_question not in ['0', '1']:
            shared_question = input("Try again: Do you want to implement shared-cable strategy?\nYes: [0]\nNo: [1]\n")
        shared = algorithms_shared_cable[algorithm][int(shared_question)]

    else:
        shared = algorithms_shared_cable[algorithm]

    """Algoritme kosten en run-time test, om de slechtste kosten en run-time in x pogingen te vinden"""

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

    if int(sys_algorithm) < 3:

        # Wil je iteratief doen?
        iterative = input("Do you want to run an iterative function?\nYes: [0]\nNo: [1]\n")

        while not iterative.isdigit() or iterative not in ['0', '1']:
            iterative = input("Input is not valid, try again:\nYes: [0]\nNo: [1]\n")

        if iterative == "0":
            attempts = input("How many times do you want to iterate? ")

            while not attempts.isdigit():
                attempts = input("Input is not an integer, try again: ")

            attempts = int(attempts)
            print("Running iterative algorithm, please wait...")
            start_time = time.time()

            for pogingen in range(attempts):
                grid = hill_climber(best_grid)

                if grid:
                    best_grid = grid
                    final_best_price = best_grid.get_total_price()

            print(f"Cost found: {final_best_price}")
            print("--- %s seconds runtime ---" % (time.time() - start_time))

<<<<<<< HEAD
    # elif sys_algorithm == '3':
    #
    #     # Wil je iteratief doen?
    #     try_steiner = input("Do you want to try steiner graph reconfiguration?\nYes: [0]\nNo: [1]\n")
    #
    #     while not try_steiner.isdigit() or try_steiner not in ['0', '1']:
    #         try_steiner = input("Input is not valid, try again:\nYes: [0]\nNo: [1]\n")
    #
    #     if try_steiner == "0":
    #         print("Running steiner algorithm, please wait...")
    #         start_time = time.time()
    #
    #         steiner(best_grid)

    batteries = best_grid.get_batteries()
    
    # for battery in batteries_best_grid:
    #     print(battery)

    # printformat = 
    # [
    #     {
    #     battery
    #         [
    #     {houses}
    #         ]
    #     }
    # ]
    counter = 0
    for battery in batteries:
        print(battery.get_remaining())
        houses = battery.get_houses()
        for house in houses:
            counter += 1

    print(counter)


=======
    best_grid.write_output(f"../data/wijk{neighbourhood}_algoritme_{sys_algorithm}.json")
>>>>>>> test
    draw(best_grid)

if __name__=="__main__":
    main()