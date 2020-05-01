"""
sleepy
version 1.0 28.04.2020
geschrieben von Robert Armand Bedard

Dieses Programm lässt den Computer sich für eine kurze Zeit von seinen täglichen Strapazen ausruhen,
indem ihm etwas erholsamer Schlaf gegeben wird.
Die Wartezeit wird überbrückt mit lustigen, blauen Punkten,
die am Ende des Programmes wieder entfernt werden.

"""
import os #importiert os für die spätere Löschung des Bildschirms
import time #importiert time für die Schlummerfunktion sleep(float)

def cls(): #plattformunabhängige Funktion zur Löschung des Bildschirms 
    os.system("cls" if os.name == "nt" else "clear") #"cls" für Windows Systeme, clear für die meisten anderen

"""
Nun gelangen wir zur Nutzereingabe, die als Wert schlafen(int) gespeichert wird
"""
while True:
    try :
        schlafen = int(input("Wie lange wird es dauern? ")) # schlafen (int) gibt die Schlafdauer in Sekunden an
        break
    except ValueError:
        print("bitte nur ganze Zahlen eingeben: ") # hier wird sichergestellt, dass die Eingabe vom Format int ist

punkte = 1 # punkte(int) steht für die Anzahl der auszugebenden Punkte
cls() #Bildschirm wird gelöscht

while punkte <= schlafen: #Schleife wird durchlaufen, bis punkte <= schlafen

    for x in range(punkte):
        print("\x1B[36m . \x1B[0m", end = "") #Ausgabe der Punkte in einer Zeile
    print("") # hier wird angezeigt, dass die Zeile nun beendet ist
    time.sleep(1) # hier lassen wir das Programm für eine Sekunde schlafen
    punkte += 1
    cls() # wieder wird der Bildschirm gelöscht

print("\033[91m\033[1mFertig!\nDer Computer hat sich etwas erholt! \033[0m") #gut für den Computer

