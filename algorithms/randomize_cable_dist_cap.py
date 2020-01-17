from .randomize_dist_cap import find_battery
from .randomize import randomize_objects

def rand_cable_dist_cap(grid):
    """
    Algoritme die ook naar bestaande gelegde kabels kijkt, en de de kabel/batterij kiest met minste afstand
    """
    huizen = grid.get_huizen()
    batterijen = grid.get_batterijen()

    randomize_objects(huizen, batterijen)

    # Voor huis in huizen
    for huis in huizen:

        # Zoek de dichtsbijzijndste batterij
        batterij = find_battery(batterijen, huis)

        # Bereken de afstand tussen de beste batterij en huis
        afstand_batterij = huis.distance(batterij)

        # Base-line afstand kabel (Upper-bound)
        beste_afstand_kabel = 1000000

        # Declaratie beste kabel
        beste_kabel = tuple

        # Loop door de batterijen array
        for b in batterijen:

            # Pak de resterende capaciteit van elke batterij
            resterend = b.get_resterend()

            # Als de batterij uberhaupt verbindingen heeft, anders prune
            if not b.is_empty():

                # Als de batterij capaciteit nog voldoet, anders prune
                if resterend >= huis.get_output():

                    # Pak de unieke kabels die aan de batterij is aangesloten
                    kabels = b.get_unieke_kabels()

                    # Loop door deze unieke kabels
                    for k in kabels:
                        afstand_kabel = huis.distance(k)

                        # Als de afstand van de kabel beter is dan de beste afstand die geconstateerd is
                        if afstand_kabel < beste_afstand_kabel:

                            # Zet dan deze kabel als de beste
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