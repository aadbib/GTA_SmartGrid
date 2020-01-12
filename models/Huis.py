# Model voor Huis
class Huis:

    prijs_kabel = 9

    # Constructor & attributen
    def __init__(self, loc, out):
        self.__locatie = tuple(loc.split(', '))
        self.__output = float(out)
        self.__kabels = []

    # Getters & Setters
    def get_locatie(self):
        return self.__locatie

    def get_output(self):
        return self.__output

    def get_kabels(self):
        return self.__kabels

    def set_kabels(self, kabel):
        self.__kabels.append(kabel)

    def bereken_prijs_kabels(self):
        return (len(self.get_kabels()) - 1) * Huis.prijs_kabel

    # Afstand huis - batterij
    def distance(self, batterij):
        distance_y = abs(int(batterij.get_locatie()[1]) - int(self.__locatie[1]))
        distance_x = abs(int(batterij.get_locatie()[0]) - int(self.__locatie[0]))

        return distance_x + distance_y

    # toString()
    def __str__(self):
        return f'Locatie: {self.__locatie}, Output: {self.__output}, Kabels: {self.__kabels}'

    def __repr__(self):
        return f'Locatie: {self.__locatie}'