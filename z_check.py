"""
z_check
version 1.0
geschrieben am 22.04.2020 von Robert Armand Bedard
Dieses Programm prüft sowohl, ob eine Eingabe vom format int ist, 
als auch ob sie gerade, positiv 
und mit einer bestimmten Zahl teilbar ist


"""

#Ausgabe des Programmprofils
print("""
z_check
version 1.0 22.04.2020
geschrieben von Robert Armand Bedard

z_check erlaubt dir zu prüfen, 
ob eine eingegebene Zahl positiv ist
und ob sie sich durch eine weitere, frei wählbare Zahl teilen lässt

......................................................

""")


#Eingabe der Variablen wunsch_zahl als und teiler als int
while True:
    try:
        wunsch_zahl = input("Gib eine ganze Zahl ein, die du von z_check prüfen lassen willst: ")
        wunsch_zahl = int(wunsch_zahl)
        break
    except ValueError:
        print("Es sind momentan leider nur ganze Zahlen erlaubt")
        print("Wir arbeiten noch an eine Implementierung von Zebras.")

while True:
    try:
        teiler = input("Gib eine weitere ganze Zahl ein, durch welche du die erste teilen lassen möchtest: ")
        teiler = int(teiler)
        break
    except ValueError:
        print("Es sind momentan leider nur ganze Zahlen erlaubt")
        print("Wir arbeiten noch an eine Implementierung von Zebras.")

#nun wird geprüft ob wunsch_zahl positiv ist und das ergebnis sogleich ausgegeben
print()
if wunsch_zahl < 0:
    print( str(wunsch_zahl) + " ist negativ!")
elif wunsch_zahl == 0:
    print("Du hast 0 eingegeben z_check empfiehlt dir, über deine Eingabe zu kontemplieren.")
else:
    print( str(wunsch_zahl) + " ist positiv!")
print()
#Nun wird geprüft, ob wunsch_zahl durch teiler teilbar ist
rest = wunsch_zahl % teiler
if rest == 0:
    print("Hurra, " + str(wunsch_zahl) + " ist durch "
    + str(teiler) + " teilbar!")
else:
    print("Es betrübt z_check, dir mitteilen zu müssen, "
    + "dass " + str(wunsch_zahl) + " nicht durch "
    + str(teiler) + " teilbar ist!")



