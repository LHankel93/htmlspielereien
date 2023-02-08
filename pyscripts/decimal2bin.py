import sys

# Python Skript um Dezimal-Zahlenwerte in Binär-Zahlensystem umzuwandeln

# Parameter zu Variable zuweisen

if len(sys.argv) > 1:
    input = sys.argv[1]
else:
    input = int(425)

# Prüfen ob Parameter/Variable numerisch ist
if input:
    input = int(input)
    # Hier mit der Konvertierung anfangen
    # Anzahl Stellen herausfinden
    dezZwei = input
    anzahlStellen: int = 0
    while dezZwei != 0:
        dezZwei = dezZwei / 2
        anzahlStellen = anzahlStellen + 1
    zahlen = []
    for i in range(anzahlStellen):
        zahlen.append(input % 2)
        input = input / 2

    for x in zahlen:
        print(zahlen[x])
