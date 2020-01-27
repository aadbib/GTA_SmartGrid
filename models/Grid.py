# Importeer libraries
import csv
from .House import House
from .Battery import Battery
import json

class Grid:

    # Statische attributen
    big_steps = 10
    small_steps = 1
    start_axis = -1
    end_axis = 52

    # Constructor & attributen
    def __init__(self, neighbourhood, house_file, battery_file):
        self.__neighbourhood = neighbourhood
        self.__segmenten = []
        self.__batteries = []
        self.__houses = []
        self.ending_x = 50
        self.ending_y = 50
        self.load_objects(house_file, battery_file)

    # Functie: Laadt huis en batterij objecten van bestanden
    def load_objects(self, *argv):

        # Open bestanden en maak een reader
        houses_neighbourhood = open(argv[0])
        batteries_neighbourhood = open(argv[1])
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

    # Getters & setters
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

    def set_battery(self, battery):
        self.__batteries.append(battery)

    def get_houses(self):
        return self.__houses

    def clear_all_cables_batteries(self):
        for battery in self.__batteries:
            houses = battery.get_houses()

            for house in houses:
                house.clear_cables()

    def clear_unique_cables_batteries(self):
        for battery in self.__batteries:
            battery.clear_unique_cables()

    def clear_batteries(self):
        self.__batteries.clear()

    def get_segmenten(self):
        return self.__segmenten

    def set_segment(self, segment):
        self.__segmenten.append(segment)

    # Functie: Zet gegevens om in JSON-formaat en schrijf naar een bestand
    def write_output(self, file):
        json_file = open(file, 'w')
        json_output = []

        for battery in self.__batteries:

            info = battery.dictify()
            json_output.append(info)

        json_file.write(json.dumps(json_output, indent=2))


    # toString()
    def __str__(self):
        return f"{self.__batteries}"