from algorithms.randomize import randomize_objects

def find_best_battery(batterijen, huis):
    """
    Zoekt de verste batterij voor een gegeven huis, waarbij de output niet uitmaakt
    """
    optimale_index = 0
    min_afstand = 101

    for index, batterij in enumerate(batterijen):
        try:
            afstand_batterij = huis.distance(batterij)

            if afstand_batterij < min_afstand:
                optimale_index = index
                min_afstand = afstand_batterij

        except IndexError:
            pass

    return batterijen[optimale_index]


def best_dist_no_capacity_restrictions(grid):
    """
    Algoritme die de slechtse batterij voor een huis linkt
    """
    huizen = grid.get_huizen()
    batterijen = grid.get_batterijen()
    for huis in huizen:
        batterij = find_best_battery(batterijen, huis)
        batterij.lay_cable_to_house(huis)

def best_dist_no_cap_shared_cable(grid):
    """
    Algoritme die ook naar bestaande gelegde kabels kijkt, en de de kabel/batterij kiest met minste afstand
    """
    huizen = grid.get_huizen()
    batterijen = grid.get_batterijen()

    randomize_objects(huizen, batterijen)

    # Voor huis in huizen
    for huis in huizen:

        # Zoek de dichtsbijzijndste batterij
        batterij = find_best_battery(batterijen, huis)

        # Bereken de afstand tussen de beste batterij en huis
        afstand_batterij = huis.distance(batterij)

        # Base-line afstand kabel (Upper-bound)
        beste_afstand_kabel = 1000000

        # Declaratie beste kabel
        beste_kabel = tuple

        # Loop door de batterijen array
        for b in batterijen:

            # Pak de unieke kabels die aan de batterij is aangesloten
            kabels = b.get_unieke_kabels()

            # Loop door deze unieke kabels
            for k in kabels:
                afstand_kabel = huis.distance(k)

                # Als de afstand van de kabel beter is dan de beste afstand die geconstateerd is
                if afstand_kabel < beste_afstand_kabel:
                    # Zet dan dan deze kabel als de beste
                    beste_afstand_kabel = afstand_kabel

                    # Onthoud de tuple/locatie van deze kabel
                    beste_kabel = k

                    # Onthoud van welke batterij deze kabel komt
                    batterij_kabel = b

        # Als de afstand van deze kabel dichterbijer ligt dan de afstand van de dichtsbijzijnste batterij
        if beste_afstand_kabel < afstand_batterij:
            batterij_kabel.set_huis(huis)

            # Leg kabel vanuit huis naar deze dichtsbijzijndste kabel
            huis.lay_cable_to_cable(beste_kabel, batterij_kabel)

        # Anders sluit aan de dichtsbijzijnste batterij
        else:
            batterij.lay_cable_to_house(huis)