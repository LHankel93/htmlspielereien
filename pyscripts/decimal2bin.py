import sys

# Python Skript um Dezimal-Zahlenwerte in Binär-Zahlensystem umzuwandeln

# Parameter zu Variable zuweisen

if len(sys.argv) > 1:
    input: int = sys.argv[1]
else:
    input: int = int(425)
print('Eingabe: ' + str(input))
# Hier mit der Konvertierung anfangen
# Anzahl Stellen herausfinden
dezZwei: int = input
anzahlStellen: int = 0
while dezZwei != 0:
    dezZwei: int = int(dezZwei / 2)
    anzahlStellen = anzahlStellen + 1
zahlen = []
for i in range(anzahlStellen):
    zahlen.append(input % 2)
    input = int(input / 2)

for x in zahlen:
    print(x, end = "")
    pass
