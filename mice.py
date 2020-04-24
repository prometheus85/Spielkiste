class Mice():
    """
    Diese Klasse besteht aus süßen kleinen Mäusen!
    """
    def __init__(self, name):
        self.name = name
        self.mood = 50
        self.hunger = 0
        self.lebendig = True

    def check_mood(self):
        if self.mood < 10:
            print(self.name, " ist unglücklich.")
        if self.mood in range(30,71):
            print(self.name, " ist gleichgültig.")
        else:
            print(self.name, " ist glücklich.")
    
    def check_hunger(self):
        if self.hunger > 9:
            self.lebendig = False

    def check_live(self):
        if self.lebendig == True:
            print(self.name, " ist lebendig.")
        else:
            print(self.name, " ist tot.")
    
    def pass_(self):
        self.hunger += 1

    
eingabe = input("Wie soll deine Maus heißen? : ")
benutzermaus = Mice(eingabe)
print(benutzermaus.name, " ist ein schöner Name für eine Maus!")
print("""
Um die Maus für einen Tag sich selbst zu überlassen, gib 1 ein.
Um das Spiel zu beenden, gib 2 ein
...............................................................

""")
befehl = 0

while befehl !=2:
    befehl = int(input("Was gedenkst du zu tun?"))
    if befehl == 1:
        benutzermaus.pass_()
        benutzermaus.check_hunger()
        benutzermaus.check_live()
        if not benutzermaus.lebendig:
            befehl = 2
            break
    

print("Dies ist das Ende unserer kleinen Mäusegeschichte!")
    



            
        

    



