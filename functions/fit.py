from copy import deepcopy

def fit_house_in_diamond(houses_copy, batteries):
    """Functie om huizen die nog over zijn, efficient aan een batterij te koppelen"""

    # Output huis die overgebleven is
    output_missing_house = houses_copy[0].get_output()

    # Sorteer batterijen resterend capaciteit hoog > laag, en selecteer meest_resterende batterij
    batteries.sort(key=lambda battery: battery.get_remaining(), reverse=True)
    copy_batteries = deepcopy(batteries)
    copy_batteries.pop(0)
    battery_with_most_capacity = batteries[0]
    capacity_battery_most = battery_with_most_capacity.get_remaining()

    # Blijf loopen, en huizen efficient verwisselen, tot het huis in de batterij past
    for battery in copy_batteries:

        second_most_battery_capacity = battery
        capacity_battery_second = second_most_battery_capacity.get_remaining()

        # Kijk naar de huizen in de eerst batterij en pak hoogste output
        houses_first_battery = battery_with_most_capacity.get_houses()
        house_most_output = max(houses_first_battery, key=lambda house: house.get_output())
        house_first_index = houses_first_battery.index(house_most_output)
        output_house_most = house_most_output.get_output()

        # Kijk naar de huizen in de tweede batterij
        houses_second_battery = second_most_battery_capacity.get_houses()
        second_index_house = None
        second_house_output = 100
        least_remaining_battery_2 = 100

        # Pak het huis met een output dat ervoor zorgt dat missende huis past
        for index, house in enumerate(houses_second_battery):
            output_house = house.get_output()
            remaining_battery_2 = capacity_battery_second - (output_house_most - output_house)

            # Let hierop dat de eerste en tweede batterij de wissel aankunnen en dat er in één wissel genoeg ruimte is voor het missende huis
            if remaining_battery_2 < least_remaining_battery_2 and remaining_battery_2 >= 0:
                second_house_output = output_house
                second_index_house = index
                least_remaining_battery_2 = remaining_battery_2

        # Verwissel de huizen van de batterijen
        houses_first_battery.pop(house_first_index)
        second_house = houses_second_battery.pop(second_index_house)
        houses_first_battery.append(second_house)
        houses_second_battery.append(house_most_output)

        if output_missing_house < battery_with_most_capacity.get_remaining():
            houses_first_battery.append(houses_copy.pop(0))
            break