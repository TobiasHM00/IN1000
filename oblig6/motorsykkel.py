class Motorsykkel:                                                                                                                      #klasse motorsykkel
    def __init__(self, merke, registreringsnummer, kilometerstand):                                                                     #konduktør
        self._merke = merke                                                                                                             #lager en variabel for merket
        self._kilometerstand = kilometerstand                                                                                           #lager en variabel for kilomaterstand
        self._registreringsnummer = registreringsnummer                                                                                 #lager en variabel for registreringsnummer

    def kjor(self,km):                                                                                                                  #metode for å legge til km
        self._kilometerstand += km                                                                                                      #legger til antall km sendt inn 

    def hentKilometerstand(self):                                                                                                       #metode for å hente kilometerstand
        return self._kilometerstand                                                                                                     #returner kilometerstand
    
    def skrivUt(self):                                                                                                                  #metode for utskrift
        print("Merke:", self._merke, "Registreringsnummer:", self._registreringsnummer, "Kilometerstand:", self._kilometerstand)        #utskriftslinje