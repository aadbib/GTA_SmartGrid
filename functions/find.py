def find_house(battery, houses):
    """
        Zoekt het dichtstbijzijndste huis voor een gegeven batterij,
        waarbij de output in de resterende capaciteit past
    """
    optimal_index = None
    min_distance = 100

    for index, house in enumerate(houses):
        output_house = house.get_output()

        distance_house = house.distance(battery)

        if distance_house < min_distance:
            remaining = battery.get_remaining()

            if remaining >= output_house:
                optimal_index = index
                min_distance = distance_house

    # Als de output niet meer voloet, return dan niks (en niet de 1e huis van huizen met index 0)
    try:
        house = houses[optimal_index]

        # Pop als deze huis geen exception throwed/raised
        houses.pop(optimal_index)
        return house

    except:
        pass


def find_battery(batteries, house):
    """
        Zoekt het dichtstbijzijndste batterij voor een gegeven huis,
        waarbij de output in de resterende capaciteit past
    """
    optimal_index = 0
    min_distance = 100
    output_house = house.get_output()

    for index, battery in enumerate(batteries):
        distance_battery = house.distance(battery)

        if distance_battery < min_distance:
            remaining = battery.get_remaining()

            if remaining >= output_house:
                optimal_index = index
                min_distance = distance_battery

    return batteries[optimal_index]


def find_best_battery(batteries, house):
    """
        Zoekt de beste batterij voor een gegeven huis,
        waarbij de output niet uitmaakt
    """
    optimal_index = 0
    min_distance = 101

    for index, battery in enumerate(batteries):
        try:
            distance_battery = house.distance(battery)

            if distance_battery < min_distance:
                optimal_index = index
                min_distance = distance_battery

        except IndexError:
            pass

    return batteries[optimal_index]


def find_worst_battery(batteries, house):
    """
        Zoekt de verste batterij voor een gegeven huis,
        waarbij de output niet uitmaakt
    """
    worst_index = 0
    max_distance = 0

    for index, battery in enumerate(batteries):
        try:
            distance_battery = house.distance(battery)

            if distance_battery > max_distance:
                worst_index = index
                max_distance = distance_battery

        except IndexError:
            pass

    return batteries[worst_index]
