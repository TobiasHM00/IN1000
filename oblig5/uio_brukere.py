'''
Programmet lager brukernavn og eposter utifra navnet og suffixen man skriver inn
'''
def lagBrukernavn(navn):                                                                                        #funkjson som lager brukernavn
    liste = navn.split()                                                                                        #splitter fornavn og etternavn
    etternavn = liste[1][0]                                                                                     #henter første bokstav i etternavnet
    brukernavn = liste[0] + etternavn[0]                                                                        #lager brukernavn ved fornavn og førtseboktav
    return brukernavn                                                                                           #returnerer brukernavnet

def lagEpost(brukernavn, suffix):                                                                               #funksjon som lager epost
    epost = brukernavn + "@" + suffix                                                                           #lager epost ved brukernavn og suffix
    return epost                                                                                                #returnerer epost

def skrivUtEpost(ordbok):                                                                                       #funksjon som går gjennom ordbok og skriver ut
    for nøkkel in ordbok:                                                                                       #løkke som går gjennom ordbok
        liste = lagEpost(nøkkel, ordbok[nøkkel])                                                                #skriver ut eposten etter at den har kalt på lagEpost funkjsonen
    return liste                                                                                                #returnerer liste

def hovedprogram():                                                                                             #prosedyre som gjør det lettere å holde kontroll
    dict = {}                                                                                                   #tom ordbok
    brukerinput = input("Skriv enten i(input), p(print) eller s(stop) og se hva som skjer: ")                   #brukerinput
    while brukerinput != "s":                                                                                   #løkke som sjekker hva brukerinputen er
        if brukerinput == "i":                                                                                  #sjekker hvis brukerinput er i
            navn = input("Skriv et navn med fornavn og ett etternavn: ").lower()                                #brukerinput til navn, bruker lower sånn at porblemet med store eller små bokstaver er løst
            brukernavn = lagBrukernavn(navn)                                                                    #variabel der man kaller på lagBrukernavn med navnet om argument
            suffix = input("Skriv en suffix (eks: gmail.com, hotmail.com): ").lower()                           #brukerinput til suffix, bruker lower sånn at porblemet med store eller små bokstaver er løst
            dict[brukernavn] = suffix                                                                           #legger inn brukernavn og suffix i ordboken
            brukerinput = input("Skriv enten i(input), p(print) eller s(stop) og se hva som skjer: ")           #brukerinput som spør igjen som sørger for at løkken kjører på nytt
        elif brukerinput == "p":                                                                                #hvis brukerinput er p
            print("Eposten er: " , skrivUtEpost(dict))                                                          #kaller på skrivUtEpost for å skrive ut epost
            brukerinput = input("Skriv enten i(input), p(print) eller s(stop) og se hva som skjer: ")           #brukerinput som spør igjen som sørger for at løkken kjører på nytt
        else:                                                                                                   #hvis brukerinput er ingen av alternativene
            brukerinput = input("Skriv enten i(input), p(print) eller s(stop) og se hva som skjer: ")           #brukerinput som spør igjen som sørger for at løkken kjører på nytt
    print("Du tastet s og programmet sluttet.")                                                                 #utskrift hvis brukerinput er s
        
hovedprogram()                                                                                                  #kaller på hovedprogrammet for å starte programmet

'''
Dette ble brukt tidligere i oppgaven så kommenterte det vekk
Skal dette være med i den endelige koden som man leverer inn?
epost = lagEpost(brukernavn, suffix)
print(brukernavn)
print(epost)
'''