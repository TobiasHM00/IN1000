'''
I dette programmet bruker vi lister til å sjekke om et navn er satt inn i listen eller ikke.
Den første listen er er bare for å lære litt hvordan lister fungerer
'''
liste = [5,8,13]                                    #lager en liste med 3 tall
liste.append(6)                                     #legger til ett tall på slutten av listen
print(liste[0], liste[2])                           #printer ut det første og tredje elementet

navnliste = []                                      #definerer en tom liste
navnliste.append(input("Skriv et navn: "))          #ber brukeren skrive inn ett navn og setter det inn i listen
navnliste.append(input("Skriv et navn: "))          #ber brukeren skrive inn ett navn og setter det inn i listen
navnliste.append(input("Skriv et navn: "))          #ber brukeren skrive inn ett navn og setter det inn i listen
navnliste.append(input("Skriv et navn: "))          #ber brukeren skrive inn ett navn og setter det inn i listen

if "Tobias" in navnliste:                           #en if sjekk som skal sjekke om mitt navn er satt inn i listen
    print("Du husket meg!")                         #skriver ut en melding hvis brukeren har skrevet mitt navn
else:                                               #hvis ikke han har skrevet inn navnet mitt må jeg sjekke det
    print("Du glemte meg!")                         #skriver så ut en passende melding til at brukeren har glemt navnet mitt

nyliste = []                                        #definerer en ny lister
sum = liste[0]+liste[1]+liste[2]                    #legger sammen alle objektene i listen
produkt = liste[0]*liste[1]*liste[2]                #multipliserer alle ovjektene i listen
nyliste.append(sum)                                 #legger sum verdien inn i den nye listen
nyliste.append(produkt)                             #legger inn produktet inn i den nye listen

nyliste_og_liste = []                               #definerer enda en ny liste
nyliste_og_liste = liste + nyliste                  #legger den opprinnelige tallisten og den nye men summen og produktet inn i den tredje listen
print(nyliste_og_liste)                             #skriver ut den nye samlede listen
nyliste_og_liste.pop()                              #fjerner det siste objektet i listen
nyliste_og_liste.pop()                              #fjerner det siste objektet i listen
print(nyliste_og_liste)                             #skriver ut listen som er igjen
