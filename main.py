import sys
import time
from models.Grid import Grid
from algorithms.Random import Random
from algorithms.Greedy import Greedy
from algorithms.Best import Best
from algorithms.Worst import Worst
from algorithms.Diamond import Diamond
from algorithms.Hillclimber import Hillclimber
from visualisation.plot_grid import draw

# Variabele die functie-referenties van de algoritmen opslaan
random_algorithm = Random.rand_one_to_one_algorithm
greedy_no_shared = Greedy.dist_cap_algorithm
greedy_shared = Greedy.rand_cable_dist_cap
best_no_shared_restrict_off = Best.best_dist_no_capacity_restrictions
best_shared_restrict_off = Best.best_dist_no_cap_shared_cable
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
    if neighbourhood not in ['1', '2', '3']:
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

    # Map input-waarde aan functie-referenties
    algorithms = {
        '1': random_algorithm,
        '2': greedy_no_shared,
        '3': greedy_shared,
        '4': worst_algorithm,
        '5': best_no_shared_restrict_off,
        '6': best_shared_restrict_off,
        '7': diamond_algorithm
    }
    algorithm = algorithms[sys_algorithm]

    # Map functie referenties met wel/geen gedeelde kabels
    algorithms_shared_cable = {
        random_algorithm: False,
        greedy_no_shared: False,
        greedy_shared: True,
        worst_algorithm: [True, False],
        best_no_shared_restrict_off: False,
        best_shared_restrict_off: True,
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

    # Base-line worst-case, best-case, houd gegevens bij
    worst_price = 0
    final_best_price = 1000000
    best_grid = None
    print("Running algorithm, please wait...")
    start_time = time.time()

    for attempt in range(attempts):
        grid = Grid(neighbourhood, f"../data/wijk{neighbourhood}_huizen.csv", f"../data/wijk{neighbourhood}_batterijen.csv")
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

    # Wil je iteratief doen?
    if int(sys_algorithm) < 3:
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

    best_grid.write_output(f"../data/wijk{neighbourhood}_algoritme_{sys_algorithm}.json")
    draw(best_grid)

if __name__=="__main__":
    main()