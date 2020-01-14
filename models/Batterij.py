# Model voor Batterij
class Batterij:

    batterij_prijs = 5000
    prijs_kabel = 9

    # Constructor & attributen
    def __init__(self, loc, cap):
        self.__locatie = loc.replace('[', '').replace(']', '').replace(' ', '').split(',')
        self.__capaciteit = float(cap)
        # Todo: Set maken, zodat je zeker weet dat huizen uniek aan batterij aangesloten zijn
        self.__huizen = []
        self.__unieke_kabels = set({})

    # Getters & Setters
    def get_locatie(self):
        return self.__locatie

    def is_empty(self):
        return len(self.__unieke_kabels) == 0

    def get_capaciteit(self):
        return self.__capaciteit

    def get_huizen(self):
        return self.__huizen

    def get_unieke_kabels(self):
        return self.__unieke_kabels

    def set_unieke_kabel(self, kabel):
        self.__unieke_kabels.add(kabel)

    def set_huis(self, huis):
        if huis not in self.__huizen:
            self.__huizen.append(huis)

    def get_resterend(self):
        aangesloten = 0

        for huis in self.__huizen:
            aangesloten += huis.get_output()

        return self.__capaciteit - aangesloten

    def total_price(self):
        totale_prijs = 0

        for huis in self.__huizen:
            totale_prijs += huis.bereken_prijs_kabels()

        totale_prijs += Batterij.batterij_prijs

        return totale_prijs

    def unieke_total_price(self):
        return ((len(self.get_unieke_kabels()) - 1) * Batterij.prijs_kabel) + Batterij.batterij_prijs

    def lay_cable(self, huis):
        distance_y = int(self.__locatie[1]) - int(huis.get_locatie()[1])
        distance_x = int(self.__locatie[0]) - int(huis.get_locatie()[0])
        huis_y = int(huis.get_locatie()[1])
        huis_x = int(huis.get_locatie()[0])
        batterij_y = int(self.__locatie[1])

        if distance_y > 0:

            for movement in range(abs(distance_y)):
                huis.set_kabels((huis_x, huis_y + movement))
                self.set_unieke_kabel((huis_x, huis_y + movement))
        else:

            for movement in range(abs(distance_y)):
                huis.set_kabels((huis_x, huis_y - movement))
                self.set_unieke_kabel((huis_x, huis_y - movement))

        if distance_x > 0:

            for movement in range(abs(distance_x) + 1):
                huis.set_kabels((huis_x + movement, batterij_y))
                self.set_unieke_kabel((huis_x + movement, batterij_y))
        else:

            for movement in range(abs(distance_x) + 1):
                huis.set_kabels((huis_x - movement, batterij_y))
                self.set_unieke_kabel((huis_x - movement, batterij_y))

        self.set_huis(huis)

    # toString()
    def __str__(self):
        return f'Locatie: {self.__locatie}, Capaciteit: {self.__capaciteit}, Huizen: {self.__huizen}, Resterend: {self.get_resterend()}'

    def __repr__(self):
        return f'Locatie: {self.__locatie}'
