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
            print("Ny varmerekord på", dag, maaned, "med en temperatur på", ordbok[maaned], "grader")   #utskrifts linje
    minfil.close()                                                                                      #lukker filen min
    return nyordbok                                                                                     #returnerer den nye ordboken

def hovedprogram():                                                                                     #definerer hovedprosedyre
    ordbok = lesfil("max_temperatures_per_month.csv")                                                   #setter en variabel lik kallet til første funksjon
    print(ordbok)                                                                                       #skriver ut ordboken
    nyordbok = sjekktemp(ordbok, "max_daily_temperature_2018.csv")                                      #setter en variabel lik kallet til andre funksjon
    print(nyordbok)                                                                                     #skriver ut den nye ordboken

hovedprogram()                                                                                          #kaller på hovedprosedyren og starter prgrammet