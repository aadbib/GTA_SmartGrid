# Model voor Batterij
class Batterij:

    batterij_prijs = 5000

    # Constructor & attributen
    def __init__(self, loc, cap):
        self.__locatie = loc.replace('[', '').replace(']', '').split(',')
        self.__capaciteit = float(cap)
        self.__huizen = []

    # Getters & Setters
    def get_locatie(self):
        return self.__locatie

    def get_capaciteit(self):
        return self.__capaciteit

    def get_huizen(self):
        return self.__huizen

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

    # toString()
    def __str__(self):
        return f'Locatie: {self.__locatie}, Capaciteit: {self.__capaciteit}, Huizen: {self.__huizen}, Resterend: {self.get_resterend()}'

