'''
I dette programmet bruker jeg løkker og lister til å registrere steder, klesplagg og avreisedato
'''
steder = []                                                                                         #lager en tom sted-liste
klesplagg = []                                                                                      #lager en tom liste til klesplagg
avreisedato = []                                                                                    #lager en tom liste til avreisedato
for sted in range(5):                                                                               #bruker en løkke som kjører 5 ganger
    steder.append(input("Skriv et reisemål: "))                                                     #legger til hva brukeren skriver inn i listen for steder
    klesplagg.append(input("Skriv et klesplagg: "))                                                 #legger til det brukeren skriver inn i listen for klesplagg
    avreisedato.append(input("Skriv en avreisedato: "))                                             #legger til det brukeren skriver inn i lsiten for avreisedato

reiseplan = [steder, klesplagg, avreisedato]                                                        #legger de tre listene inn i en samlet liste

for indeks in reiseplan:                                                                            #bruker en løkke for å gå gjennom listene
    print(indeks)                                                                                   #printer ut hele reisemål listen

liste_indeks1 = int(input("Skriv et tall: "))                                                       #spør om en indeks fra brukeren

if liste_indeks1 in range(0,3):                                                                     #sjekker om den første indeksen er 0, 1 eller 2
    liste_indeks2 = int(input("Skriv et tall: "))                                                   #ber om enda et tall fra brukeren for å bruke som indeks
    if liste_indeks2 in range(0,5):                                                                 #sjekker om indeksen er 0, 1, 2, 3 eller 4
        print(reiseplan[liste_indeks1][liste_indeks2])                                              #hvis begge indeksene er gyldige skriver jeg ut hva som står på den indeksplassen
    else:
        print("Ugyldig input. Prøve et input mellom 0 og 4")                                        #hvis indeks nummer 2 ikke er gyldig kommer dette ut
else:
    print("Ugyldig input. Prøv først et tall mellom 0 og 2, også et tall mellom 0 og 4")            #hvis ingen av indeksene er gyldige kommer dette ut
