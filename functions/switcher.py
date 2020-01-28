from random import choice

def switch_houses_hillclimber(all_indexes_all_batteries, all_batteries):
    """Verwisselt huizen van twee set batterijen"""

    # Pak twee sets, onthoud alles
    battery1_index = choice(all_indexes_all_batteries)
    all_indexes_all_batteries.remove(battery1_index)
    battery1 = all_batteries[battery1_index]
    battery1_houses = battery1.get_houses()
    house1 = choice(battery1_houses)
    house1_index = battery1_houses.index(house1)

    battery2_index = choice(all_indexes_all_batteries)
    all_indexes_all_batteries.remove(battery2_index)
    battery2 = all_batteries[battery2_index]
    battery2_houses = battery2.get_houses()
    house2 = choice(battery2_houses)
    house2_index = battery2_houses.index(house2)

    # Verwijder de huizen uit de batterij-huizen array en leg kabels
    battery1.remove_house(house1_index)
    battery2.remove_house(house2_index)
    battery1.lay_cable_to_house(house2)
    battery2.lay_cable_to_house(house1)

    return battery1, battery2