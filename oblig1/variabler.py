'''
Programmet skriver ut informasjon enten jeg har valgt eller ber brukeren sette inn i variabler.
Bruker en blanding av variabler, print og input funksjonene til å få dette til en terminal.
'''
navn = input("Hva er navnet ditt? ")                #Fikk beskjed at brukeren skulle gi variabelen "navn" en verdi også skrive det ut
print("Hei", navn,)                                 #Brukte derfor input for å lagre en verdi brukeren kunne gi også skrive den ut men print funksjonen

tallEn = 8                                          #En ny variabel med en heltallverdi
tallTo = 5                                          #En ny variabel med en heltallverdi
print(tallEn)                                       #Skriver ut en av tallverdiene
print(tallTo)                                       #Skriver ut den andre tallverdien
differanse = tallEn - tallTo                        #Lagrer differansen av de to tallverdiene i en variabel
print("Differanse:", differanse,)                   #Skriver ut denne differansen med print

navnTo = input("Skriv enda et navn: ")              #Fikk beskjed om at brukeren skulle gi en ny variabel en verdi og siden brukeren skal gjøre det må vi bruke en input funksjon
sammen = navn + navnTo                              #Tar å lagrer de to variablene med navn i en variabel
print(sammen)                                       #Skriver ut denne samlede variabelen
sammenTo = navn + " og " + navnTo                   #Lager en ny variabel der jeg fikser et mellomrom og "og" mellom de to navnene
print(sammenTo)                                     #Skriver ut den nye og forbedrede variabelen av den tidligere samlede variabelen
