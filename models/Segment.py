class Segment:

    # Statische attributen
    id = 0
    x_size = 10
    y_size = 10

    # Constructor & attributen
    def __init__(self, sp, ep):
        self.__starting_point = sp
        self.__end_point = ep
        self.__battery = None
        self.__id = Segment.id
        Segment.id += 1

    # Getters & setters
    def get_starting_point(self):
            return self.__starting_point

    def get_end_point(self):
            return self.__end_point

    def get_location_segment(self):
        return f'(x: {self.__starting_point[0]}-{self.__end_point[0]} y: {self.__starting_point[1]}-{self.__end_point[1]})'

    def get_id(self):
        return self.__id

    def get_battery(self):
        return self.__battery

    def set_battery(self, battery):
        self.__battery = battery

    def __str__(self):
        return f"{self.__id}: {self.__starting_point} - {self.__end_point}, {self.__battery}"

    def __repr__(self):
        return f"{self.__id}: {self.__battery}"