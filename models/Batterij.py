# Model voor Batterij
class Batterij:

    # Constructor & attributen
    def __init__(self, loc, cap):
        self.__locatie = loc
        self.__capaciteit = cap
        self.__huizen = []

    # Getters & Setters
    def get_locatie(self):
        return self.__locatie

    def get_capaciteit(self):
        return self.__capaciteit

    def get_huizen(self):
        return self.__huizen

    def set_huis(self, huis):
        self.__huizen += huis

    # toString()
    def __str__(self):
        return f'Locatie: ${self.__locatie}, Capaciteit: ${self.__capaciteit}, Huizen: ${self.__huizen}'

