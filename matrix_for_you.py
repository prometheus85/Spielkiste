"""
matrix_for_you
version 1.2020.05.07
geschrieben von Robert Armand Bedard
special thanks to love

"""

import numpy as np # numpy wird importiert als np
import math # math wird für die wurzelfunktion gebucht
import random # random brauchen wir für unsere hübsche Zufallsmatrix

wurzelvektor = np.array([math.sqrt(n) for n in range(1, 6)]) # ein vektor

neuner_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) # eine 3*3-Matrix

def matrix_generator():
    """
    Diese Funktion generiert eine 3*3-Matrix mit zufallsgenerierten Einträgen zwischen 1 und 9
    Sie kommt ohne Argument klar.
    returnt ist ein array

    """
    return np.array([[random.randint(1, 9) for x in range(3)] for y in range(3)])

def vektor_summe(vektor):
    """
    Diese Funktion bestimmt die Summe eines Vektors
    Argument = list, array, dic, tupel oder dergleichen
    return = str
    """
    return sum(vektor)

def matrix_diagonalprodukt(matrix):
    """
    Diese Funktion bestimmt das Produkt der Diagonalelemente einer Matrix
    Argument = array[3,3]
    return = float
    """
    return matrix[0, 0] * matrix[1, 1] * matrix[2, 2]

def matrix_generator_n(n):
    """
    generiert eine n*n-Matrix wobei sich die Einträge aus der Multiplikation der Zeilen- und Spaltenindizes
    Argument = int
    return = array[n,n]
    """
    return np.array([[x*y for x in range(1, n + 1)] for y in range(1, n + 1)])

def matrix_spalte(spalte, matrix):
    """
    Diese Funktion gibt eine beliebige Spalte einer beliebigen n*n-Matrix aus
    Argument (spalte = int , matrix = array
    """
    return [matrix[spalte, x] for x in matrix[0]-1] # Erstellung einer Spalte als liste

def matrix_zeile(zeile, matrix):
    """Diese Funktion gibt eine beliebige Zeile einer beliebigen n*n-Matrix aus
    Argument (spalte = int , matrix = array
    """
    return matrix[zeile]

print("""

......................................................
matrix_for_you
version 0.2020.05.05
geschrieben von Robert Armand Bedard
special thanks to love
......................................................

""")



# Nun wird die Summe der Einträge von wurzelvektor berechnet
print("Die Summe der Einträge des Vekors ", 
    list(wurzelvektor),  
    " beträgt ",  
    vektor_summe(wurzelvektor))

zufalls_matrix_1 = matrix_generator() # Generierung der Zufallsmatrix zufalls_matrix_1
print("Generiere Zufallsmatrix")
print(zufalls_matrix_1)
print("Das Produkt der Diagonaleinträge beträgt ", matrix_diagonalprodukt(zufalls_matrix_1))

while True: # Schleife, die den Nutzer nach der Größe matrix_size der Matrix fragt und sicher stellt, dass nur ganze positive Zahlen angegeben werden
    try:
        matrix_size = int(input("Geben sie n für die Generierung einer n*n-Matrix ein: "))
        if matrix_size <= 0:
            print("Wie stellst du dir das vor? Nur ganze, positive Zahlen sind erlaubt")
        else:
            break
    except ValueError:
        print("Überprüfe doch noch einmal, ob deine Eingabe wirklich Sinn gemacht hat!")

print("""
..............................................

Generiere deine Wunschmatrix

..............................................
""")

n_matrix = matrix_generator_n(matrix_size) # generiere n_matrix der Größe matrix_size
print("Wunschmatrix")
print()
print(n_matrix)

n_matrix_block = np.array([[n_matrix[0, 0], n_matrix[0, 1]], [n_matrix[1, 0], n_matrix[1, 1]]])

print()
print("2*2 Block:")
print()
print(n_matrix_block)

print()
print("Es ist Zeit für eine Sezession!")
hauptroutine = True
while hauptroutine == True: # Diese Schleife läuft, bis der nutzer "exit" eingibt
    while True: # wir stellen sicher, dass die Spaltenangabe auch eine positive, ganze Zahl ist
        try:
            n_matrix_spalte = int(input("Welche Spalte willst du abtrennen? ")) - 1
            if n_matrix_spalte < 0 or n_matrix_spalte > matrix_size-1:
                print("Vielleicht war das mit der Sezession doch keine so gute Idee...")
                print("Wir brauchen ganze, positive Zahlen, die trotzdem nicht größer sind, als die Matrix selbst.")
            else:
                break
        except ValueError:
            print("Vielleicht sollten wir das ganze Unterfangen lieber vergessen. Wir bräuchten doch ganze, positive Zahlen!")

    wunsch_spalte = matrix_spalte(n_matrix_spalte, n_matrix)
    print()
    print("Die ", n_matrix_spalte+1, ". Spalte deiner Wunschmatrix lautet:")
    print()
    print(wunsch_spalte)
    input()
    while True: # wir stellen sicher, dass die Zeilenangabe auch eine positive, ganze Zahl ist
        try:
            n_matrix_zeile = int(input("Welche Zeile willst du abtrennen? ")) - 1
            if n_matrix_zeile < 0 or n_matrix_zeile > matrix_size-1:
                print("Vielleicht war das mit der Sezession doch keine so gute Idee...")
                print("Wir brauchen ganze, positive Zahlen, die trotzdem nicht größer sind, als die Matrix selbst.")
            else:
                break
        except ValueError:
            print("Vielleicht sollten wir das ganze Unterfangen lieber vergessen. Wir bräuchten doch ganze, positive Zahlen!")

    wunsch_zeile = matrix_zeile(n_matrix_zeile, n_matrix)
    print()
    print("Die ", n_matrix_zeile + 1, " Zeile deiner persönlichen, einzigartigen Wunschmatrix,\n", 
        "lautet:")
    print()
    print(wunsch_zeile)

    weiter = input("Wollen wir das ganze nochmal machen? Falls du die Lust verloren hast, gebe einfach exit ein. ")
    if weiter == "exit":
        hauptroutine = False
print()
print("Auf Wiedersehen")





