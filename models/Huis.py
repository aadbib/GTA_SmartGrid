# Model voor Huis
class Huis:

    # Constructor & attributen
    def __init__(self, loc, out):
        self.__locatie = loc
        self.__output = out
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

    # toString()
    def __str__(self):
        return f'Locatie: {self.__locatie}, Output: {self.__output}, Kabels: {self.__kabels}'