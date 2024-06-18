'''
Programmet bruker funskjoner og assert for å sjekke om det vil bli riktig
'''
def addisjon(tall1, tall2):                     #definerer en funskjon
    return tall1 + tall2                        #gjør ut regning og returnerer resultat

def subtraksjon(tall1, tall2):                  #definerer en funksjon
    return tall2 - tall1                        #gjør ut regning og returnerer resultat

def divisjon(tall1, tall2):                     #definerer en funksjon
    return tall1 / tall2                        #gjør ut regning og returnerer resultat

def tommerTilCm(antallTommer):                  #definerere en funksjon
    assert antallTommer > 0                     #sjekker om argumentet er større enn 0
    return antallTommer * 2.54                  #gjør ut regning og returnerer resultat

def skrivBeregninger():                                             #definerer en prosedyre
    inp1 = float(input("Skriv tall 1: "))                           #brukerinput 1
    inp2 = float(input("Skriv tall 2: "))                           #brukerinput 2
    print("Resultat av summering: ", addisjon(inp1,inp2))           #skriver ut resultatet på funksjonen addisjon med brukerinputtene
    print("Resultat av subtraksjon: ", subtraksjon(inp1,inp2))      #skriver ut resultatet på funksjonen subtraksjon med brukerinputtene
    print("Resultat av divisjon: ", divisjon(inp1,inp2))            #skriver ut resultatet på funksjonen divisjon med brukerinputtene
    print()                                                         #linjeskift
    print("Om gjøring fra tomme til cm:")                           #en forklaring
    inp3 = float(input("Skriv et tall: "))                          #brukerinput 3
    print("Resultat: ", tommerTilCm(inp3), "cm")                    #skriver ut resultatet på funksjonen tommerTilCm med brukerinput 3
    

print(addisjon(6,9))                            #skriver ut resultat

assert addisjon(7,8) == 15                      #sjekker om funksjonen vil gjøre riktig
assert addisjon(-5,-9) == -14                   #sjekker om funksjonen vil gjøre riktig
assert addisjon(7,-3) == 4                      #...

assert subtraksjon(3,7) == 4                    #...
assert subtraksjon(-6,-2) == 4                  #...
assert subtraksjon(4,-8) == -12                 #...

assert divisjon(4,2) == 2                       #...
assert divisjon(-10,-2) == 5                    #...
assert divisjon(-9,3) == -3                     #sjekker om funksjonen vil gjøre riktig

print(tommerTilCm(12), "cm")                    #skriver ut resultat

skrivBeregninger()                              #kaller på prosedyren
