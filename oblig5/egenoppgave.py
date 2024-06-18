'''
Skriv et beregningsprogram for skreddere med en
funksjon som leser inn en fil der hver linje beskriver et navn på et mål og selve målet i tommer.
Bruk den vedlagte filen dress_lengder.txt
Du kan bruke funksjonen .split() for å gjøre dette.
La programmet legge disse målene i en ordbok med navn på målet som nøkkelverdi
og returner ordboken. Lag deretter en prosedyre som tar imot en liste av mål og
benytter seg av tommerTilCm som du skrev tidligere for å skrive ut målene i centimeter.
Lag også muligheten til å kunne legge til nye linjer i filen og avslutte programmet. Sjekk om brukerinputen er gyldig eller ikke
'''
def lagordbok(filnavn):                                                                         #definerer en funksjon
    ordbok = {}                                                                                 #tom ordbok
    minfil = open(filnavn)                                                                      #åpner filen
    for linje in minfil:                                                                        #løkke som går gjennom linjene
        biter = linje.split()                                                                   #deler opp linjene i biter
        navn_på_mål = biter[0]                                                                  #setter første bit som den variablen
        tomme = float(biter[1])                                                                 #setter andre bit til variabelen som et flyttall
        ordbok[navn_på_mål] = tomme                                                             #setter det inn i ordboken
    minfil.close()                                                                              #lukker filen
    return ordbok                                                                               #returnerer ordboken

def regntommetilcm(listeTomme):                                                                 #definerer ny funksjon
    listeCM = []                                                                                #tom liste
    for tomme in listeTomme:                                                                    #løkke som kjører gjennom listen verdiene i tommer
        listeCM.append(tomme*2.54)                                                              #utregner til cm og legger i liste
    print("Liste med verdiene i cm", listeCM)                                                   #utskrift med listen

def leggTilDressLengde(filnavn, ordbok):                                                        #definerer en ny funksjon
    fil = open(filnavn, "a")                                                                    #åpner den andre filen
    kroppsDel = input("Skriv et sted på kroppen som skal måles (husk mellomrom): ")             #spør om en del på kroppen som skal måles
    while kroppsDel in ordbok:                                                                  #løkke som sjekker om 
        return print("Du har allerede målt denne delen!")                                       #returnerer hvis den er i ordboken
        
    lengde = input("Skriv en lengde i tomme: ")                                                 #variabel for lengden og spør om det fra bruker
    fil.write("\n")                                                                             #skriver en ny linje til fil
    fil.write(kroppsDel), fil.write(lengde)                                                     #skriver inn kroppsdel og lengden til fil
    fil.close()                                                                                 #lukker fil

def hovedprogram():
    print("Hei. I dette programmet kan du få legge til nye dress lengder og hvor lange de er eller regne ut hvor langt det er i cm.")       #print som forklarer litt
    print("Her har du en ordbok med nåværende dress lengder")                                   #print som forklarer litt 
    ordbok = lagordbok("dress_lengder.txt")                                                     #lager en ordbok med kall til riktig funksjon
    print(ordbok)                                                                               #skriver ut ordboken
    print("Hva vil du gjøre?")                                                                  #print som spør brukeren
    print("Skriv 'legge' hvis du vil legge til mer i ordboken. Skriv 'regn' hvis du vil regne om fra tomme til cm."         #print som forklarer litt
    "Skriv 'slutt' hvis du vil avslutte programmet.")
    inp = input("")                                                                             #brukerinput
    while inp != "slutt":                                                                       #løkke som sjekker brukerinputen
        if inp == "regn":                                                                       #sjekk som sjekker brukerinput
            listeTomme = []                                                                     #tom liste til verdier i cm
            for verdi in ordbok:                                                                #løkke som går gjennom løkken
                listeTomme.append(ordbok[verdi])                                                #legger til verdiene i ordboken i en liste
            regntommetilcm(listeTomme)                                                          #kaller på prosedyren og sender listen
        elif inp == "legge":                                                                    #sjekker hvis inp er legge
            leggTilDressLengde("dress_lengder.txt", ordbok)                                     #kaller på funskjson med filnavn og ordboken
            print("Her har du den nye ordboken:")                                               #print funk
            ordbok = lagordbok("dress_lengder.txt")                                             #setter ordbok lik kallet for å ersatte den gamle ordboken me de nye veriene
            print(ordbok)                                                                       #skriver ut ordboken 
        else:
            print("Du skrev noe ugyldig!")                                                      #skriver ut når det er ugyldig bruker inp
        
        print("Skriv 'legge' hvis du vil legge til mer i ordboken. Skriv 'regn' hvis du vil regne om fra tomme til cm." 
        "Skriv 'slutt' hvis du vil avslutte programmet.")                                       #print som forklarer litt
        inp = input("")                                                                         #brukerinput som sørger for oppdatert brukerinput

hovedprogram()                                                                                  #kall på hovedprosedyre
print("Du avsluttet programmet")                                                                #print funk