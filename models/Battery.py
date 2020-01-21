# Model voor Batterij
class Battery:

    battery_price = 5000
    price_cable = 9

    # Constructor & attributen
    def __init__(self, loc, cap):
        self.__location = loc.replace('[', '').replace(']', '').replace(' ', '').split(',')
        self.__capacity = float(cap)
        # Todo: Set maken, zodat je zeker weet dat huizen uniek aan batterij aangesloten zijn
        self.__houses = []
        self.__unique_cables = set({})

    # Getters & Setters
    def get_location(self):
        return self.__location

    def is_empty(self):
        return len(self.__unique_cables) == 0

    def get_capacity(self):
        return self.__capacity

    def get_houses(self):
        return self.__houses

    def get_unique_cables(self):
        return self.__unique_cables

    def set_unique_cable(self, cable):
        self.__unique_cables.add(cable)

    def clear_unique_cables(self):
        self.__unique_cables.clear()

    # Voor iteratief opnieuw unieke kabels leggen
    def set_unique_cables_iterative(self):
        for house in self.__houses:
            cables = house.get_cables()

            for c in cables:
                self.__unique_cables.add(c)

    def set_house(self, house):
        self.__houses.append(house)

    def get_remaining(self):
        attached = 0

        for house in self.__houses:
            attached += house.get_output()

        return self.__capacity - attached

    def total_price_battery(self):
        total_price = 0

        for house in self.__houses:
            total_price += house.calculate_price_cables()

        total_price += Battery.battery_price

        return total_price

    def unique_total_price(self):
        return ((len(self.__unique_cables) - 1) * Battery.price_cable) + Battery.battery_price

    def lay_cable_to_house(self, house):
        distance_y = int(self.__location[1]) - int(house.get_location()[1])
        distance_x = int(self.__location[0]) - int(house.get_location()[0])
        house_y = int(house.get_location()[1])
        house_x = int(house.get_location()[0])
        battery_y = int(self.__location[1])

        if distance_y > 0:

            for movement in range(abs(distance_y)):
                house.set_cables((house_x, house_y + movement))
                self.set_unique_cable((house_x, house_y + movement))
        else:

            for movement in range(abs(distance_y)):
                house.set_cables((house_x, house_y - movement))
                self.set_unique_cable((house_x, house_y - movement))

        if distance_x > 0:

            for movement in range(abs(distance_x) + 1):
                house.set_cables((house_x + movement, battery_y))
                self.set_unique_cable((house_x + movement, battery_y))
        else:

            for movement in range(abs(distance_x) + 1):
                house.set_cables((house_x - movement, battery_y))
                self.set_unique_cable((house_x - movement, battery_y))

        self.set_house(house)

    # toString()
    def __str__(self):
        return f'Location: {self.__location}, Capacity: {self.__capacity}, Houses: {self.__houses}, Remaining: {self.get_remaining()}'

    def __repr__(self):
        return f'Location: {self.__location}'
