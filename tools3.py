""" Programm zur Berechnung des größten gemeinsamen Teilers zweier natürlicher Zahlen
"""

def ggt(n, m):
    while (n % m) != 0:
        n, m = m, (n % m)
    else:
        return m
    
print (ggt(8, 14))