'''
I dette programmet definerer vi en prosedyre hvor vi henter inn et navn og et bosted
Når det er gjort kaller jeg på prosedyren 3 ganger
'''
def prosedyre():                                        #definerer en prosedyre og gir den et navn
    navn = input("Hva er navnet ditt? ")                #skal hente inn et navn som brukeren gir og bruker input til en variabel
    bosted = input("Hvor bor du? ")                     #gjør det samme bare om et bosted
    print("Hei " + navn + ", du bor i", bosted)         #bruker print for å skrive det ut

prosedyre()                                             #kaller på prosedyren
prosedyre()                                             #kaller på prosedyren
prosedyre()                                             #kaller på prosedyren
