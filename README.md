# GTA_SmartGrid NOG NIET AF

Project programmeertheorie minor prog

Groene energie is de energie van de toekomst, en zelf produceren is de mode van nu. Veel huizen hebben tegenwoordig zonnepanelen, windmolens of andere installaties om zelf energie mee te produceren. Fortuinlijk genoeg produceren die installaties vaak meer dan voor eigen consumptie nodig is. Het overschot zou kunnen worden terugverkocht aan de leverancier, maar de infrastructuur (het grid) is daar veelal niet op berekend. Om de pieken in consumptie en productie te kunnen managen moeten er batterijen geplaatst worden.

## Aan de slag
### Vereisten
Alle code is geschreven in Python 3.7. Om een wijkrooster te kunnen tekenen moet er mathplotlib bibliotheek geïnstalleerd worden. Alle uitleg daarover bevindt zich in requirements.txt. Hierbij een korte instructie:

>pip install -r requirements.txt

### Gebruik
Het programma wordt gestart door het volgende aan te roepen:
>python main.py <"wijk"> <"algoritme"> <"pogingen">

Waarbij:
* <"wijk"> staat voor het wijknummer (1, 2 of 3)
* <"algoritme"> staat voor het type algoritme dat wordt gedraaid (beschrijving van de naam-algoritmes staat hieronder):
    * 1: Random
    * 2: Greedy
    * 3: Shared_Greedy
    * 4: Kostenbovengrens
    * 5: Kostenondergrens als kabels niet gedeeld zijn
    * 6: Kostenondergrens als kabels gedeeld zijn
    * 7: Diamond
* <"pogingen"> staat voor het aantal iteraties waarmee een bepaald algoritme zich herhaalt


### Structuur
* **/GTA_SmartGrid:** bevat alle code van dit project
    * **/GTA_SmartGrid/algorithms:** bevat de code voor alle algoritmes
    * **/GTA_SmartGrid/data:** bevat de huizen- en batterijengegevens van alledrie wijken
    * **/GTA_SmartGrid/functions:** bevat allerlei toegepaste functies
    * **/GTA_SmartGrid/images:** bevat roostericoontjes
    * **/GTA_SmartGrid/models:** bevat de vier benodigde klassen voor deze casus
    * **/GTA_SmartGrid/visualisation:** bevat de code voor de visualisatie


### Opdracht

De batterijen kosten 5000 per stuk. De kabels kosten 9 per grid-segment. De kabels liggen op de gridlijnen, mogen ook gridpunten met een huis passeren, en de afstand van een huis tot een batterij wordt berekend volgens de manhattan distance.
Er moet dus een netwerk aangelegd worden dat alle huizen verbindt aan een batterij en de kosten zo minimaal mogelijk laat zijn.
De opdracht heeft twee delen:
* zonder kabels delen
* kabels kunnen gedeeld worden: meerdere huizen kunnen via 1 kabel verbonden worden

### Klassen

* House: stelt een huis-object op aan de hand van ingelade locatie en output. De aangesloten kabels zijn opgeslagen als een "instance" hiervan.
* Battery: stelt een batterij-object op aan de hand van ingelade locatie en capaciteit. De huizen die aan een bepaalde batterij verbonden zijn, worden als "instance" opgeslagen.
* Segment: stelt een segment-object op aan de hand van start- en eind-coördinaten. Wordt gebruikt bij Diamond-algoritme met een batterij als een "instance".
* Grid: stelt een grid-object op met alle huizen en batterijen erin.

### Algoritmes
#### Oplossingsalgoritmes

* Random:
sluit een willekeurig huis aan een willekeurige batterij
* Greedy:
sluit een willekeurig huis aan een dichtstbijzijndste batterij met resterende capaciteit
* Hillclimber (bordurend op Random en Greedy):
verbetert de voornoemde twee algoritmes door twee willekeurige huizen van twee willekeurige batterijen te wisselen, controlerend of er een verbetering mogelijk is
* Shared_Greedy:
sluit een willekeurig huis aan een dichtstbijzijndste batterij met resterende capaciteit gegeven dat kabels gedeeld kunnen worden
* Diamond:
sluit alle dichtstbijzijndste huizen aan de buitenste batterij met resterende capaciteit gegeven dat kabels gedeeld kunnen worden

#### Toestandsruimtealgoritmes

* Kostenbovergrens:
sluit een willekeurig huis aan een verste batterij (mogelijk voor gedeelde en niet gedeelde gevallen), geen rekening houdend met resterende capaciteit
* Kostenondergrens als kabels niet gedeeld zijn:
sluit een willekeurig huis aan een dichtstbijzijndste batterij voor het niet-gedeelde geval, geen rekening houdend met resterende capaciteit
* Kostenondergrens als kabels gedeeld zijn:
sluit een willekeurig huis aan een dichtstbijzijndste batterij voor het gedeelde geval, geen rekening houdend met resterende capaciteit


### Auteurs

* George Soroko
* Tom van Esseveld
* Achraf Adbib

### Dankbetuigingen

Quinten van der Post voor advies en toezicht.