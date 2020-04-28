"""
sleepy
version 1.0 28.04.2020
geschrieben von Robert Armand Bedard

Dieses Programm lässt den Computer sich für eine kurze Zeit von seinen täglichen strapazen ausruhen,
indem ihm etwas erholsamen Schlaf gegeben wird.
Die Wartezeit wird überbrückt mit lustigen, blauen Punkten,
die am Ende des Programmes wieder entfernt werden.

"""
import os #importiert os für die spätere Löschung des Bildschirms
import time #importiert time für die zeitliche Beschränkung des Schlummers

while True:
    try :
        schlafen = int(input("Wie lange wird es dauern? ")) # schlafen (int) gibt die Schlafdauer in Sekunden an
        break
    except ValueError:
        print("bitte nur ganze Zahlen eingeben: ")

for x in range(schlafen):
    print("\x1B[31m . \x1B[0m", end = "")
    time.sleep(1)
   

os.system("cls")
print("Der Computer hat sich etwas erholt!")
