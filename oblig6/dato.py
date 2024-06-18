class Dato:                                                                                                             #definerer klassen min
    def __init__(self, nyDag, nyMaaned, nyttAar):                                                                       #konduktøren til klassen
        self._nydag = nyDag                                                                                             #variabel for dag
        self._nymaaned = nyMaaned                                                                                       #variabel for måneden
        self._nyttaar = nyttAar                                                                                         #variabel for år

    def lesAar(self):                                                                                                   #metode for å lese år
        return self._nyttaar                                                                                            #returnerer år

    def utskrift(self):                                                                                                 #metode for å skrive ut datoen
        utskrivning = "Datoen er: " + str(self._nydag) + "." + str(self._nymaaned) + "." + str(self._nyttaar)           #utskriftssetning
        return utskrivning                                                                                              #returner utskriften

    def sjekkDag(self, tall):                                                                                           #metode for å sjekke dagen
        if tall == self._nydag:                                                                                         #sjekker om dag er lik argumentet som ble med inn i metoden
            return True                                                                                                 #returnerer True
        return False                                                                                                    #returnerer False
    
    def sjekkDato(self, dato):                                                                                          #metode for å sjekke datoene
        datoliste = dato.split(".")                                                                                     #splitter tekststrengen av dato
        if int(datoliste[2]) <= self._nyttaar:                                                                          #sjekker om innsendt dato har et lavere årstall
            if int(datoliste[1]) <= self._nymaaned:                                                                     #sjekker om innsendt dato har et lavere månedstall
                if int(datoliste[0]) < self._nydag:                                                                     #sjekker om innsendt dato har en lavere dato dag
                    print("Den første datoen er etter den andre!")                                                      #print setning
                else:                                                                                                   #hvis dagen til innsendt dato er høyere enn objektdato så
                    print("Den nye datoen er etter den første datoen!")                                                 #print setning
            else:                                                                                                       #hvis måneden til innsendt dato er høyere enn objekt måned så
                print("Den nye datoen er etter den første datoen!")                                                     #print setning
        else:                                                                                                           #hvis året til innsendt dato er høyere enn objekt år så
            print("Den nye datoen er etter den første datoen!")                                                         #print setning
            
    def endreDato(self):                                                                                                #metode for å endre datoen har med dag skifte, måneds skifte (forskjelle på 30 og 31 dager pluss februar med 28 dager men ikke for skuddår) og årskifte
        liste30dag = [4,6,9,11]                                                                                         #liste for måneder med 30 dager
        liste31dag = [1,3,5,7,8,10,12]                                                                                  #liste for måneder med 31 dager
        if self._nydag == 30:                                                                                           #sjekker om dag er 30 
            if self._nymaaned in liste30dag:                                                                            #if True så sjekker den om måneden er i listen for 30 dager 
                self._nydag = 1                                                                                         #hvis det er sant sett dag til en
                self._nymaaned += 1                                                                                     #plusse måneden med 1
            else:                                                                                                       #hvis ikke
                self._nydag += 1                                                                                        #legge 1 til dagen
        elif self._nydag == 31:                                                                                         #sjekker om dagen er 31
            if self._nymaaned in liste31dag:                                                                            #hvis sant sjekker om måneden er i listen for 31 dager
                self._nydag = 1                                                                                         #hvis sant sette dagen til 1
                if self._nymaaned == 12:                                                                                #må sjekke om man er på slutten av året
                    self._nymaaned = 1                                                                                  #hvis ja sette måneden til 1
                    self._nyttaar += 1                                                                                  #og plusse året med 1
                else:                                                                                                   #hvis ikke
                    self._nymaaned += 1                                                                                 #legge 1 til måneden
        elif self._nymaaned == 2:                                                                                       #må sjekke om måneden er 2 for det er et spesial tilfelle
            if self._nydag == 28:                                                                                       #sjekke om dagen er 28
                self._nydag = 1                                                                                         #hvis ja sette dagen til 1
                self._nymaaned += 1                                                                                     #og legge 1 til måneden
        else:                                                                                                           #hvis ikke
            self._nydag += 1                                                                                            #legge 1 til dagen