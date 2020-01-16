from .randomize import randomize_objects

def find_worst_battery(batterijen, huis):
    """
    Zoekt de verste batterij voor een gegeven huis, waarbij de output niet uitmaakt
    """
    slechtste_index = 0
    max_afstand = 0

    for index, batterij in enumerate(batterijen):
        try:
            afstand_batterij = huis.distance(batterij)

            if afstand_batterij > max_afstand:
                slechtste_index = index
                max_afstand = afstand_batterij

        except IndexError:
            pass

    return batterijen[slechtste_index]


def worst_dist_no_capacity_restrictions(grid):
    """
    Algoritme die de slechtse batterij voor een huis linkt
    """
    huizen = grid.get_huizen()
    batterijen = grid.get_batterijen()
    for huis in huizen:
        batterij = find_worst_battery(batterijen, huis)
        batterij.lay_cable_to_house(huis)


def worst_dist_no_cap_shared_cable(grid):
    """
    Algoritme die ook naar bestaande gelegde kabels kijkt, en de de kabel/batterij kiest met minste afstand
    """
    huizen = grid.get_huizen()
    batterijen = grid.get_batterijen()

    randomize_objects(huizen, batterijen)

    # Voor huis in huizen
    for huis in huizen:

        # Zoek de slechtste batterij
        batterij = find_worst_battery(batterijen, huis)

        # Bereken de afstand tussen de slechtste batterij en huis
        afstand_batterij = huis.distance(batterij)

        # Base-line afstand kabel (Upper-bound)
        slechtste_afstand_kabel = 0

        # Declaratie slechtste kabel
        slechtste_kabel = tuple

        # Loop door de batterijen array
        for b in batterijen:

            # Pak de unieke kabels die aan de batterij is aangesloten
            kabels = b.get_unieke_kabels()

            # Loop door deze unieke kabels
            for k in kabels:
                afstand_kabel = huis.distance(k)

                # Als de afstand van de kabel meer is dan de slechtste afstand die geconstateerd is
                if afstand_kabel > slechtste_afstand_kabel:

                    # Zet dan dan deze kabel als de slechtste
                    slechtste_afstand_kabel = afstand_kabel

                    # Onthoud de tuple/locatie van deze kabel
                    slechtste_kabel = k

                    # Onthoud van welke batterij deze kabel komt
                    batterij_kabel = b

        # Als de afstand van deze kabel verder ligt dan de afstand van de verste batterij
        if slechtste_afstand_kabel > afstand_batterij:
            batterij_kabel.set_huis(huis)

            # Leg kabel vanuit huis naar deze verste kabel
            huis.lay_cable_to_cable(slechtste_kabel, batterij_kabel)

        # Anders sluit aan de verste batterij
        else:
            batterij.lay_cable_to_house(huis)