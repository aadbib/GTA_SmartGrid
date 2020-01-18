# Importeer libraries
import csv
from .House import House
from .Battery import Battery

# Model Grid
class Grid:

    # Static attributen
    big_steps = 10
    small_steps = 1
    start_axis = -1
    end_axis = 52

    def __init__(self, neighbourhood, house_file, battery_file):
        self.__neighbourhood = neighbourhood
        self.__batteries = []
        self.__houses = []
        self.load_objects(house_file, battery_file)

    def load_objects(self, *argv):

        houses_neighbourhood = open(argv[0])
        batteries_neighbourhood = open(argv[1])

        # DictReader
        reader = csv.DictReader(houses_neighbourhood)

        # Loop door csv-reader, maak huis-objecten aan
        for line in reader:
            house = House(f"{line['x']},{line[' y']}", line[' max output'])
            self.__houses.append(house)

        houses_neighbourhood.close()
        reader = csv.DictReader(batteries_neighbourhood)

        # Loop door csv-reader, maak batterij-objecten aan
        for line in reader:
            battery = Battery(line['positie'], line[' capaciteit'])
            self.__batteries.append(battery)

        batteries_neighbourhood.close()

    def get_total_price(self):
        final_price = 0

        for battery in self.__batteries:
            final_price += battery.total_price_battery()

        return final_price

    def get_unique_total_price(self):
        final_price = 0

        for battery in self.__batteries:
            final_price += battery.unique_total_price()

        return final_price

    def get_batteries(self):
        return self.__batteries

    def get_houses(self):
        return self.__houses

    def clear_unique_cables_batteries(self):
        for battery in self.__batteries:
            battery.clear_unique_cables()

    def __str__(self):
        # toString()
        return f"Grid voor de wijk: {self.__neighbourhood},\nHuizen: {self.__houses},\nBatterijen: {self.__batteries}"