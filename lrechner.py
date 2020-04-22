"""
Dieses Programm wurde geschrieben von robert Armand Bedard in der Nacht zwischen dem 21. und 22.04.2020
Es trägt den Namen lrechner, der für Lohnrechner steht und eben diesen Zweck erfüllen soll.

"""

print("""

lrechner: dein Programm um das netto vom brutto zu berechnen
version 1.0 22.04.2020
geschrieben von Robert Armand Bedard
""")

"""
als erstes erfolgt die Abfrage nach Stundenlohn, 
Arbeitsstunden pro Monat und monatliche Abgaben in Prozent

"""
while True:
    try:
        slohn = (input("Gib deinen Stundenlohn ein: "))
        slohn = float(slohn)
        break
    except ValueError:
        print("Es sind nur Dezimalzahlen erlaubt!")
     
while True:
    try:
        astunden = (input("Gib die Stundenzahl ein, in denen du je Monat arbeitest : "))
        astunden = int(astunden)
        break
    except ValueError:
        print("Es sind nur ganze Zahlen erlaubt!")

while True:
    try:
        abgaben = (input("Gib deine monatlichen Lohnabgaben in Prozent als Dezimalzahl ein : "))
        abgaben = float(abgaben)
        break
    except ValueError:
        print("Es sind nur Dezimalzahlen erlaubt!")

#Ausgabe der Nutzereingabe
print("""
.................................................................

""")
print("Du arbeitest "
    + str(astunden) 
    + " Stunden pro Monat.")
print("Dein Stundenlohn beträgt hierbei " 
    + str(slohn) + " Euro.")
print("Deine Abgaben betragen "
    + str(abgaben) + " Prozent deines Monatslohns")

#Es folgt die Berechnung des Brutto - und des Nettoeinkommens
b_einkommen = slohn * astunden
n_einkommen = b_einkommen * float(1 - abgaben/100)

#Und zu guter Letzt, die Ausgabe des Ergebnisses
print("")
print("Dein Bruttomonatslohn beträgt "
    + str(b_einkommen)
    + " Euro.")
print("Dein Nettomonatslohn beträgt "
    + str(n_einkommen)
    + " Euro.")
print("""

Vielen Dank, dass du dich für lrechner entschieden hast,
die clevere Art, das Netto vom Brutto zu berechnen.
Dieses Programm wurde ohne Zuhilfenahme eines Kängurus geschrieben!""")


