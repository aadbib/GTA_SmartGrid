from .Batterij import Batterij
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

    # Afstand huis - batterij of kabel
    def distance(self, batterij):

        # Als het een batterij betreft
        if isinstance(batterij, Batterij):
            distance_y = abs(int(batterij.get_locatie()[1]) - int(self.__locatie[1]))
            distance_x = abs(int(batterij.get_locatie()[0]) - int(self.__locatie[0]))

        # Als het een kabel betreft
        else:
            distance_y = abs(int(batterij[1]) - int(self.__locatie[1]))
            distance_x = abs(int(batterij[0]) - int(self.__locatie[0]))

        return distance_x + distance_y

    # Afstand huis - kabel
    # def distance_cable(self, kabel):
    #     return distance_x + distance_y

    # Todo: Maak functie die een huis aan een kabel aansluit
    def lay_cable(self, kabel):
        distance_y = int(self.__locatie[1]) - int(kabel[1])
        distance_x = int(self.__locatie[0]) - int(kabel[0])
        kabel_y = int(kabel[1])
        kabel_x = int(kabel[0])
        huis_y = int(self.__locatie[1])

        if distance_y > 0:

            for movement in range(abs(distance_y)):
                self.set_kabels((kabel_x, kabel_y + movement))
        else:

            for movement in range(abs(distance_y)):
                self.set_kabels((kabel_x, kabel_y - movement))

        if distance_x > 0:

            for movement in range(abs(distance_x) + 1):
                self.set_kabels((kabel_x + movement, huis_y))
        else:

            for movement in range(abs(distance_x) + 1):
                self.set_kabels((kabel_x - movement, huis_y))






    # toString()
    def __str__(self):
        return f'Locatie: {self.__locatie}, Output: {self.__output}, Kabels: {self.__kabels}'

    def __repr__(self):
        return f'Locatie: {self.__locatie}'