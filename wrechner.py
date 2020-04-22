"""

Dieses kleine hübsche Programm dient der Umrechnung 
von diversen gängigen Währungen gemäß der Kurse vom 21.04.2020

"""

#Festlegung der Währungskurse gemessen am US-Dollar
dollar, euro, rupie, bitcoin = ["US-Dollar", 1], ["Euro", 1.08],["Indische Rupie", 0.013], ["Bitcoin",6820]
wlist = [dollar, euro, rupie, bitcoin]

#Ausgabe des Programmnamens, 
#dessen Funktion und der verfügbaren Währungen zur Umrechnung
print("wrechner \nversion 1.0 21.04.2020")
print("geschrieben von Robert Armand Bedard")
print("""

Dieses kleine hübsche Programm dient der Umrechnung 
von diversen gängigen Währungen gemäß der Kurse vom 21.04.2020

Zu Verfügung stehen zur Zeit folgende Währungen:

0.Dollar           2.Rupie
1.Euro             3.Bitcoin

""")


#Eingabe zweier Währungen von Nutzer zum Zwecke der Umrechnung
#als ganzzahliger Wert zwischen 0 und 3

waehrung1 = int(input("Wähle die Ausgangswährung aus der Liste indem du die entsprechende Zahl zwischen 1 und 4 eingibst: "))
while not waehrung1 in range(4):
    waehrung1 = int(input("Bitte gebe eine gültige Eingabe ein: "))

waehrung2= int(input("Gib analog die Zielwährung ein: "))
while not waehrung2 in range(4):
    waehrung2 = int(input("Bitte gebe eine gültige Eingabe ein: "))

#An dieser stelle wird die Eingabe einer Währung zugeordnet
ausgangswaehrung, zielwaehrung = wlist[waehrung1], wlist[waehrung2]


#Nun geht es an die Berechnung des Wechselkurses
wkurs = ausgangswaehrung[1]/zielwaehrung[1]

#Und an dieser Stelle wird das ergebnis ausgegeben
print("Ein " + ausgangswaehrung[0] + " entspricht nach dem Stand vom 21.04.2020 " + str(wkurs) + " " + zielwaehrung[0])

#Und nun zu etwas völlig anderem
