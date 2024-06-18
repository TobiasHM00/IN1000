from datasenter import Datasenter                       #henter datasenter klassen
def hovedprogram():                                     #hovedprogram
    nyttdatasenter = Datasenter()                       #lager et datasenter objekt
    nyttdatasenter.lesInnRegneklynge("abel.txt")        #sender inn filen abel til datasenter klassen
    nyttdatasenter.lesInnRegneklynge("saga.txt")        #sender inn filen saga til datasenter klassen
    nyttdatasenter.skrivUtAlleRegneklynger()            #bruker metoden i datasenter for å skrive ut alle regneklyngene
    nyttdatasenter.skrivUtRegneklynge("saga")           #bruker metode fra datasenter sammen med et argument for å hente ut regneklyngen som argumentet er lik
hovedprogram()                                          #kaller på hovedprogrammet