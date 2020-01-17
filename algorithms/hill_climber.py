from copy import deepcopy
from random import choice

def hill_climber_algorithm(grid):
    """Algoritme die iteratief verbeteringen gaat toepassen d.m.v. de hillclimber methode"""

    # Maak een deepcopy van de grid, en leeg de set van unieke kabels voor alle batterijen
    grid_copy = deepcopy(grid)
    grid_copy.clear_unieke_kabels_batterijen()

    # Pak alle batterijen uit deze grid
    alle_batterijen = grid.get_batterijen()

    for b in alle_batterijen:

        # Todo: In hillclimber moet je niet dezelfde oplossingen gaan vergelijken, bv huis1, batterij1 vs huis2, batterij 2.
        # Todo: Zoek uit hoe je geen sets die al vergeleken zijn, niet opnieuw met elkaar vergelijkt?

        # Zorgt ervoor dat we huizen NIET uit dezelfde batterij gaan pakken en vergelijken
        alle_indexen_alle_batterijen = [0, 1, 2, 3, 4]

        # Pak twee sets, en onthoud alles
        batterij1_index = choice(alle_indexen_alle_batterijen)
        alle_indexen_alle_batterijen.remove(batterij1_index)
        batterij1 = alle_batterijen[batterij1_index]
        batterij1_huizen = batterij1.get_huizen()
        huis1 = choice(batterij1_huizen)
        huis1_index = batterij1_huizen.index(huis1)

        batterij2_index = choice(alle_indexen_alle_batterijen)
        alle_indexen_alle_batterijen.remove(batterij2_index)
        batterij2 = alle_batterijen[batterij2_index]
        batterij2_huizen = batterij2.get_huizen()
        huis2 = choice(batterij2_huizen)
        huis2_index = batterij2_huizen.index(huis2)

        # Todo: Pak de kabels/coordinaten van deze huizen, leeg ze, en haal de huizen weg van hun batterijen_array
        # Todo: Bereken opnieuw kabel/batterij afstand, maar dan met geswitchte batterijen. Dus huis-1 batterij-2, huis-2 batterij-1







