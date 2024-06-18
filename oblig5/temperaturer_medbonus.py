'''
Bruker filer til å lage en ordbok med høyeste verdier per måned og sjekke om de nye verdiene fra 2018 gjør en forskjell i ordboken
'''
def lesfil(filnavn):                                                                                    #definerer funskjon
    ordbok= {}                                                                                          #tom ordbok
    minfil = open(filnavn, "r")                                                                         #åpner den nødvendige filen
    for linje in minfil:                                                                                #løkke som kjører gjennom linjene i filen
        biter = linje.split(",")                                                                        #liste som deler det som er på hver linje ved komma
        maaned = biter[0]                                                                               #setter det første elementet lik maaned i hver linje ettersom løkken kjører
        maxtemp = float(biter[1])                                                                       #setter andre kolonne til en variabel
        ordbok[maaned] = maxtemp                                                                        #legger disse to variabelene inn i en ordbok
    minfil.close()                                                                                      #lukker filen min
    return ordbok                                                                                       #returnerer ordboken

def sjekktemp(ordbok, filnavn):                                                                         #definerer en ny funksjon
    nyordbok = ordbok                                                                                   #setter en ny ordbok lik den gammle ordboken, man kan sikkert bare sette ordbok = ordbok eller kutte hele linjen men dette hjelper meg å skille mellom de to ordbøkene
    minfil = open(filnavn, "r")                                                                         #åpner den nødvendige filen
    for linje in minfil:                                                                                #løkke som går gjennom linjene i filen min
        biter = linje.split(",")                                                                        #splitter linjene på komma og setter de i en liste
        maaned = biter[0]                                                                               #første kolonne lik måned
        dag = biter[1]                                                                                  #andre kolonne lik dag, trenger bare for utskriften i oppgave2
        temp = float(biter[2])                                                                          #tredje kolonne lik temp som flyttall                                       
        if temp > ordbok[maaned]:                                                                       #sjekker om den nye tempen er høyere enn den i ordboken
            nyordbok[maaned] = temp                                                                     #hvis den er det sette den nye tempen inn i ordboken
            print("Ny varmerekord på", dag, maaned, "med en temperatur på", nyordbok[maaned], "grader.") #utskrifts linje brukes ikke i full oppgave så kommenterte vekk
    minfil.close()                                                                                      #lukker filen min
    return nyordbok                                                                                     #returnerer den nye ordboken

def skrivTilFil(ordbok,filnavn):                                                                        #definere prosedyre med argument
    fil = open(filnavn, "w")                                                                            #åpner filen
    for indeks in ordbok:                                                                               #løkke som går gjennom ordboken
        linje = indeks + "," + str(ordbok[indeks])                                                      #definerer den linjen jeg vil skrive til fil
        fil.write(linje + "\n")                                                                         #skriver til fil
    fil.close()                                                                                         #lukker fil

def varmebølge(filnavn):                                                                                #definerer prosedyre med argument
    fil = open(filnavn, "r")                                                                            #åpner og leser filen 
    varmebølgedager = 0                                                                                 #variabel som teller hvor mange dager med varmebølge
    for linje in fil:                                                                                   #løkke som leser hver linje til fil
        biter = linje.split(",")                                                                        #deler opp hver linje i en liste
        temp = float(biter[2])                                                                          #variabel for tempen og konverterer den til et flyttall
        if temp > 25 and varmebølgedager == 0:                                                          #sjekker om temp er over 25 og om antalle dager med over 25 grader er lik 0
            bølgestart = biter                                                                          #hvis true så skal linjen være lik bølgestarten
            varmebølgedager += 1                                                                        #legge til en dag med varmebølge
        elif temp > 25:                                                                                 #hvis temp er over 25
            bølgeslutt = biter                                                                          #setter den linjen lik bølgeslutt for kan være en potensiell bølgeslutt
            varmebølgedager += 1                                                                        #legger til dag for varmebølge
        else:                                                                                           
            if varmebølgedager >= 5:                                                                    #sjekker om varmebølgedager er større eller lik 5
                print("Det er en varmebølge fra", bølgestart[1], bølgestart[0], "til", bølgeslutt[1], bølgeslutt[0],". Varmebølgen varte i", varmebølgedager, "dager") #hvis den er det så skriver den ut denne linjen
            varmebølgedager = 0                                                                         #setter varmebølge dager lik null for å finne en ny varmebølge 
    fil.close()                                                                                         #lukke fil

def hovedprogram():                                                                                     #definerer hovedprosedyre
    ordbok = lesfil("max_temperatures_per_month.csv")                                                   #setter en variabel lik kallet til første funksjon
    print(ordbok)                                                                                       #skriver ut ordboken
    nyordbok = sjekktemp(ordbok, "max_daily_temperature_2018.csv")                                      #setter en variabel lik kallet til andre funksjon
    print(nyordbok)                                                                                     #skriver ut den nye ordboken
    skrivTilFil(nyordbok, "new_max_temperatures_per_month.csv")
    varmebølge("max_daily_temperature_2018.csv")

hovedprogram()                                                                                          #kaller på hovedprosedyren og starter prgrammet