from dato import Dato                                                                       #henter klassen fra dato.py
def hovedprog():                                                                            #definerer et hovedprogram
    datoen = Dato(15,7,2019)                                                                #sender datoen til klassen
    print(datoen.lesAar())                                                                  #skriver ut året
    if datoen.sjekkDag(15):                                                                 #sjekker om dagen er 15
        print("Loenningsdag!")                                                              #hvis ja skriver ut dette
    if datoen.sjekkDag(1):                                                                  #sjekker om dagen er 1
        print("Ny maaned, nye muligheter")                                                  #hvis ja skriver ut dette
    print(datoen.utskrift())                                                                #skriver ut datoen ved hjelp av klassen
    datoen.endreDato()                                                                      #kaller på endreDato
    print(datoen.utskrift())                                                                #skriver ut ny dato
    datoen.sjekkDato(input("Skriv en dato (dag, måned, år eks. 18.7.1963) "))               #vil sjekke datoen mot en ny dato brukeren blir bedt om å skrive inn
hovedprog()                                                                                 #kaller hovedprog