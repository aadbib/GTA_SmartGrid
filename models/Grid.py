# Importeer libraries
import csv
from .Huis import Huis
from .Batterij import Batterij

# Model Grid
class Grid:

    # Static attributen
    grote_stappen = 10
    kleine_stappen = 1
    begin_as = -1
    eind_as = 52

    def __init__(self, wijk, house_file, battery_file):
        self.__wijk = wijk
        self.__batterijen = []
        self.__huizen = []
        self.load_objects(house_file, battery_file)

    def load_objects(self, *argv):

        huizen_wijk = open(argv[0])
        batterijen_wijk = open(argv[1])

        # DictReader
        reader = csv.DictReader(huizen_wijk)

        # Loop door csv-reader, maak huis-objecten aan
        for line in reader:
            huis = Huis(f"{line['x']},{line[' y']}", line[' max output'])
            self.__huizen.append(huis)

        huizen_wijk.close()
        reader = csv.DictReader(batterijen_wijk)

        # Loop door csv-reader, maak batterij-objecten aan
        for line in reader:
            batterij = Batterij(line['positie'], line[' capaciteit'])
            self.__batterijen.append(batterij)

        batterijen_wijk.close()

    def get_totale_prijs(self):
        eind_prijs = 0

        for batterij in self.__batterijen:
            eind_prijs += batterij.total_price()

        return eind_prijs

    def get_unieke_total_prijs(self):
        eind_prijs = 0

        for batterij in self.__batterijen:
            eind_prijs += batterij.unieke_total_price()

        return eind_prijs

    def get_batterijen(self):
        return self.__batterijen

    def get_huizen(self):
        return self.__huizen

    def clear_unieke_kabels_batterijen(self):
        for batterij in self.__batterijen:
            batterij.clear_unieke_kabels()

    def __str__(self):
        # toString()
        return f"Grid voor de wijk: {self.__wijk},\nHuizen: {self.__huizen},\nBatterijen: {self.__batterijen}"