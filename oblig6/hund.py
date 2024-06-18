class Hund:                                                     #klasse
    def __init__(self, alder, vekt):                            #instruktør
        self._alder = alder                                     #variabel for alder
        self._vekt = vekt                                       #variabel for vekt
        self._metthet = 10                                      #variabel for metthet
    
    def hentAlder(self):                                        #metode hentAlder
        return self._alder                                      #returnerer alderen

    def hentVekt(self):                                         #metode hentVekt
        return self._vekt                                       #returener vekt

    def spring(self):                                           #metode for spring
        self._metthet -= 1                                      #tar metthet - 1 
        if self._metthet < 5:                                   #sjekker om metthet er mindre enn 5
            self._vekt -= 1                                     #vekt - 1

    def spis(self, heltall):                                    #metode for spis med heltall argument
        self._metthet += heltall                                #legger til heltallet med metthet
        if self._metthet > 7:                                   #sjekker om metthet er større enn 7 
            self._vekt += 1                                     #legger til 1
    