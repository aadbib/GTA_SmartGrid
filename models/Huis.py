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

    # Todo: Functie schrijven van afstand huis - batterij
    def distance(self, batterij):
        distance_y = abs(int(batterij.get_locatie()[1]) - int(self.get_locatie()[1]))
        distance_x = abs(int(batterij.get_locatie()[0]) - int(self.get_locatie()[0]))

        return distance_x + distance_y

    # Todo: vind optimale batterij, criteria: capaciteit & afstand
    # Todo: Random functie zodat een random oplossing gemaakt wordt
    # Todo: Upper en lower bound definieren
    def find_battery(self, batterijen):
        output_huis = self.get_output()
        optimale_index = 0
        min_afstand = 100

        for index, batterij in enumerate(batterijen):
            try:
                afstand_batterij = self.distance(batterij)

                if afstand_batterij < min_afstand:
                    resterend = batterij.get_resterend()

                    if resterend >= output_huis:
                        optimale_index = index
                        min_afstand = afstand_batterij

            except IndexError:
                pass

        return batterijen[optimale_index]

    # toString()
    def __str__(self):
        return f'Locatie: {self.__locatie}, Output: {self.__output}, Kabels: {self.__kabels}'