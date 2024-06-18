'''
I denne oppgaven så legger vi sammen to tall og sjekker hvor mange ganger en bokstav forekommer i teksten brukerne setter inn
'''
def adder(tall1, tall2):                                                                        #definerer en prosedyre med parametere
    return "Summen av disse to tallene er ", tall1 + tall2                                      #returnerer svaret av addisjonen

summen = adder(int(input("Første tall: ")), int(input("Andre tall: ")))                         #kaller på prosedyren ved å gi den to tall som brukren oppgir og sette resultatet til en variabel
print(summen)                                                                                   #skriver ut summen
summen = adder(int(input("Første tall: ")), int(input("Andre tall: ")))                         #kaller på prosedyren ved å gi to nye tall som brukren oppgir og setter resultatet til en variabel
print(summen)                                                                                   #skriver ut den nye summen. valgte å legge en print mellom hvert fall fordi da kunne jeg bruke samme variabel og gir mer mening for brukeren

def tellForekomst(minTekst, minBokstav):                                                        #definerer en prisedyre med parametere
    tell_bokstav = 0                                                                            #må ha en variabel som teller antall bokstaver den valgte bokstaven forkommer
    indeks = 0                                                                                  #må vite hvor i teksten vi er og vite når vi er ferdig

    while indeks < len(minTekst):                                                               #bruker en løkke for å gå gjennom teksten
        if minTekst[indeks] == minBokstav:                                                      #sjekker om den valgte indeksen i teksten er lik den valgte bokstaven
            tell_bokstav += 1                                                                   #hvis det er riktig bokstav som den valgte må vi telle den
            indeks += 1                                                                         #for å bli ferdig må vi telle hvor i teksten vi er og legge til 1 for hvergang noe skjer
        else:
            indeks += 1                                                                         #må øke verdien av indeksen

    return "Bokstaven", minBokstav, "forekom", tell_bokstav, "ganger i teksten."                #returnerer et svar til kallet

forekomst = tellForekomst(input("Skriv hva som helst: "), input("Skriv en bokstav: "))          #kaller på prosedyren og setter den lik en variabel
print(forekomst)                                                                                #skriver ut denne variabelen
