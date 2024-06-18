'''
Dette er programmet er en klasse der flere sangobjekter kan bli brukt til å sjekke og få ut informasjon om sangen og til og med høre den
som er spesielt for dette programmet
'''
import simpleaudio                                                                      #henter simpleaudio for å kunne spille av
class Sang:                                                                             #klasse
    def __init__(self, artist, tittel, filnavn):                                        #konduktør
        self._tittel = tittel                                                           #instansvariabel
        self._artist = artist                                                           #instansvariabel
        self._filnavn = filnavn                                                         #instansvariabel

    def __str__(self):                                                                  #utskriftsmetode som blir kalt når man skriver 'print(objektnavn)'
        string = "Spiller " + str(self._tittel) + " av " + str(self._artist)            #utskriften
        return string                                                                   #returnerer utskriften

    def spill(self):                                                                    #metode
        print(self)                                                                     #utskrift
        wave_obj = simpleaudio.WaveObject.from_wave_file(self._filnavn)                 #henter sang ojektet og henter lydfilen
        play_obj = wave_obj.play()                                                      #spiller av lydfilen
        play_obj.wait_done()                                                            #programmet venter til lydfilen er ferdig

    def sjekkArtist(self, navn):                                                        #metode
        riktig = False                                                                  #variabel for holde kontroll på om artisten er i listen
        navnliste = navn.lower().split()                                                #lager en liste av navnet som er i argumentet
        artistliste = self._artist.lower().split()                                      #lager en liste av artist navnet i objektet som er i bruk
        for navn in artistliste:                                                        #løkke for et navn i listen med artistnavnet
            if navn in navnliste:                                                       #sjekker om navnet fra løkken er lik navnet til et element i navnliste
                riktig = True                                                           #hvis det er sånn så sette rjeg riktig til true
        return riktig                                                                   #returnerer riktig på slutten

    def sjekkTittel(self, tittel):                                                      #metode 
        if tittel.lower() == self._tittel.lower():                                      #sjekker agrument mot tittel til objektet
            return True                                                                 #if true retunerer True
        return False                                                                    #if false returnerer False

    def sjekkArtistOgTittel(self, artist, tittel):                                      #metode
        if self.sjekkArtist(artist) == True and self.sjekkTittel(tittel) == True:       #bruker de tidligere metodene for å sjekke artist og tittel
            return True                                                                 #returnerer True
        return False                                                                    #retunerer False