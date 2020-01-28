from .Battery import Battery

class House:

    price_cable = 9

    # Constructor & attributen
    def __init__(self, loc, out):
        self.__location = tuple(loc.split(', '))
        self.__output = float(out)
        self.__cables = []

    # Getters & Setters
    def get_location(self):
        return self.__location

    def get_output(self):
        return self.__output

    def get_cables(self):
        return self.__cables

    def set_cables(self, cable):
        self.__cables.append(cable)

    def clear_cables(self):
        self.__cables.clear()

    def calculate_price_cables(self):
        return (len(self.get_cables()) - 1) * House.price_cable

    # Afstand huis - batterij of kabel
    def distance(self, battery):

        # Als het een batterij betreft
        if isinstance(battery, Battery):
            distance_y = abs(int(battery.get_location()[1]) - int(self.__location[1]))
            distance_x = abs(int(battery.get_location()[0]) - int(self.__location[0]))

        # Als het een kabel betreft
        else:
            distance_y = abs(int(battery[1]) - int(self.__location[1]))
            distance_x = abs(int(battery[0]) - int(self.__location[0]))

        return distance_x + distance_y

    # Functie: Legt kabel vanuit huis naar dichtsbijzijndste kabel-coördinaat
    def lay_cable_to_cable(self, cable, battery):
        house_cable_distance_y = int(self.__location[1]) - int(cable[1])
        house_cable_distance_x = int(self.__location[0]) - int(cable[0])
        cable_y = int(cable[1])
        cable_x = int(cable[0])
        house_y = int(self.__location[1])

        if house_cable_distance_y > 0:
            for movement in range(abs(house_cable_distance_y)):
                self.set_cables((cable_x, cable_y + movement))
                battery.set_unique_cable((cable_x, cable_y + movement))

        else:
            for movement in range(abs(house_cable_distance_y)):
                self.set_cables((cable_x, cable_y - movement))
                battery.set_unique_cable((cable_x, cable_y - movement))

        if house_cable_distance_x > 0:
            for movement in range(abs(house_cable_distance_x) + 1):
                self.set_cables((cable_x + movement, house_y))
                battery.set_unique_cable((cable_x + movement, house_y))

        else:
            for movement in range(abs(house_cable_distance_x) + 1):
                self.set_cables((cable_x - movement, house_y))
                battery.set_unique_cable((cable_x - movement, house_y))

    # Functie: Zet gegevens om in JSON-formaat
    def dictify(self):
        json_dict = {}
        json_dict["location"] = f'{self.__location[0]},{self.__location[1]}'
        json_dict["output"] = self.__output
        cables_json = []

        for cable in self.__cables:
            cables_json.append(f"({cable[0]},{cable[1]})")

        json_dict["cables"] = cables_json
        return json_dict

    # toString()
    def __str__(self):
        return f'location: {self.__location}, output: {self.__output}, cables: {self.__cables}'

    def __repr__(self):
        return f'Location: {self.__location}, Output: {self.__output}, Cables: {self.__cables}'