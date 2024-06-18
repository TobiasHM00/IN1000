'''
Programmet lager brukernavn og eposter utifra navnet og suffixen man skriver inn
'''
def lagBrukernavn(navn, ordbok):                                                                                #funkjson som lager brukernavn
    liste = navn.split()                                                                                        #splitter fornavn og etternavn
    bokietter = 0                                                                                               #variabel for å telle hvilken boksatv man er på i etternavnet
    brukernavn = liste[0] + liste[len(liste)-1][bokietter]                                                      #lager brukernavn ved fornavn og førtseboktav
    while brukernavn in ordbok:                                                                                 #løkke som sier at så lenge brukernavnet er i ordboken så går den inn i løkken 
        bokietter += 1                                                                                          #teller som holder styr på hvilken bokstav i etternavnet vi er på
        brukernavn = brukernavn + liste[len(liste)-1][bokietter]                                                #setter brukernavn lik brukernavnet pluss den nye bokstaven fra etternavnets
    return brukernavn                                                                                           #returnerer brukernavnet

def lagEpost(brukernavn, suffix):                                                                               #funksjon som lager epost
    epost = brukernavn + "@" + suffix                                                                           #lager epost ved brukernavn og suffix
    return epost                                                                                                #returnerer epost

def skrivUtEpost(ordbok):                                                                                       #funksjon som går gjennom ordbok og skriver ut
    liste = []                                                                                                  #tom liste
    for nøkkel in ordbok:                                                                                       #løkke som går gjennom ordbok
        epost = lagEpost(nøkkel, ordbok[nøkkel])                                                                #variabel som sender nøkkelen i ordboken og verdien til nøkkelen
        #print(epost)                                                                                            #utskrift for epost, trenger den ikke så bare kommenterte den vekk
        liste.append(epost)                                                                                     #skriver ut eposten etter at den har kalt på lagEpost funkjsonen
    return liste                                                                                                #returnerer liste

def test_lagEpost():                                                                                            #definerer prosedyre for å sjekke lagepost
    epost = lagEpost("karin", "student.matnat.uio.no")                                                          #sender dette til funksjonen
    assert epost == "karin@student.matnat.uio.no"                                                               #hvis det vi sendte til funksjonen ikke blir lik dette kommer en assert error

def test_skrivUtEpost():                                                                                        #definerer en prosedyre for å sjekke funksjonen skrivutepost
    ordbok = {"olan": "ifi.uio.no", "karin":"student.matnat.uio.no"}                                            #lager en ordbok
    liste = skrivUtEpost(ordbok)                                                                                #sender ordboken til funksjonen 
    assert liste == ["olan@ifi.uio.no", "karin@student.matnat.uio.no"]                                          #hvis listen vi får tilbake ikke er lik dette kommer en assert error

def hovedprogram():                                                                                             #prosedyre som gjør det lettere å holde kontroll
    test_lagEpost()
    test_skrivUtEpost()
    dict = {}                                                                                                   #tom ordbok
    brukerinput = input("Skriv enten i(input), p(print) eller s(stop) og se hva som skjer: ")                   #brukerinput
    while brukerinput != "s":                                                                                   #løkke som sjekker hva brukerinputen er
        if brukerinput == "i":                                                                                  #sjekker hvis brukerinput er i
            navn = input("Skriv et navn med fornavn og ett etternavn: ").lower()                                #brukerinput til navn, bruker lower sånn at porblemet med store eller små bokstaver er løst
            brukernavn = lagBrukernavn(navn, dict)                                                              #variabel der man kaller på lagBrukernavn med navnet og ordboken som argument
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
'''
