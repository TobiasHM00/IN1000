'''
Spilleliste klassen som bruker kan bruke Sang klassen
Her samler vi alle sangene fra tekstfilen og lagrer de i en liste
'''
from sang import Sang                                                           #henter Sang klassen
class Spilleliste:                                                              #ny klasse
    def __init__(self,listenavn):                                               #konduktør
        self._sanger = []                                                       #instansvariabel for liste
        self._navn = listenavn                                                  #instansvariabel

    '''
    Jeg ser ikke noe poeng i å lage en __str__ metode for det brukes aldri print i verken denne filen eller test filen
    Det brukes bare kall til andre metoder for så å bruke __str__ metode fra sang klassen
    '''

    def lesFraFil(self,filnavn):                                                #metode
        minfil = open(filnavn)                                                  #leser fra fil
        for linje in minfil:                                                    #går gjennom filen linje for linje
            alleData = linje.strip().split(";")                                 #splitter linjen på ;
            alleData = Sang(alleData[1], alleData[0])                           #lager et nytt objekt med hver linje
            self._sanger.append(alleData)                                       #legger til hver linje i en liste
        minfil.close()                                                          #lukker programmet
        print(self)

    def leggTilSang(self,nysang):                                               #metode
       self._sanger.append(nysang)                                              #legger til sang i listen

    def fjernSang(self,sang):                                                   #metode
        self._sanger.remove(sang)                                               #fjerner sang fra listen

    def spillSang(self,sang):                                                   #metode
        sang.spill()                                                            #bruker metode fra klassen Sang til å spille sang

    def spillAlle(self):                                                        #metode
        for sang in self._sanger:                                               #løkke som går gjennom hvert element
            sang.spill()                                                        #og spiller sangen med metode fra klassen Sang
    
    def finnSang(self,tittel):                                                  #metode
        for sang in self._sanger:                                               #løkke for gå gjennom liste med sanger
            svar = sang.sjekkTittel(tittel)                                     #sender sang fra løkken til metode i klassen Sang sammen med argumentet tatt inn
            if svar == True:                                                    #sjekker om svaret fra forrige linje er True 
                return sang                                                     #returnerer sang fra løkken
        return None                                                             #returnerer None hvis sangen ikke er i listen

    def hentArtistUtvalg(self,artistnavn):                                      #metode
        sangtilartist = []                                                      #liste for sanger for en artist
        for sang in self._sanger:                                               #løkke som går gjennom liste med sanger
            svar = sang.sjekkArtist(artistnavn)                                 #sender sangen fra løkken og argumentet til metoden i klassen Sang
            if svar == True:                                                    #sjekker om det vi sendte inn er True
                sangtilartist.append(sang)                                      #legger sangen til listen med sanger for artisten
        return sangtilartist                                                    #retunerer listen med sanger for spesfikk artist