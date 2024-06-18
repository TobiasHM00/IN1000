class Person:                                                                                   #definerer en klasse
    def __init__(self, navn, alder):                                                            #kontrollør
        self._navn = navn                                                                       #klasse variabel for navn
        self._alder = alder                                                                     #klasse variabel for alder
        self._hobby = []                                                                        #klasse variabel for en tom liste
    
    def leggTilHobby(self, tekst):                                                              #metode for å legge til dato med argument
        self._hobby.append(tekst)                                                               #legger argumentet til i listen
    
    def skrivHobbyer(self):                                                                     #metode for å skrive hobbyene 
        utskrift = ""                                                                           #variabel for utskriften
        for hobby in self._hobby:                                                               #løkke som går gjennom listen med hobbyer
            utskrift += hobby + ", "                                                            #legger til hobbyen i utskriftsvariabelen
        return utskrift                                                                         #retunerer utskriften
    
    def skrivUt(self):                                                                          #metode for å skrive ut
        print("Navnet er:", self._navn, "og", self._navn, "er", self._alder, "år gammel")       #skriver ut navn og lader
        if self._hobby == []:                                                                   #sjekker hvis listen er tom
            print("Personen har ingen hobbyer")                                                 #hvis ja skriver ut dette
        else:                                                                                   #hvis ikke
            print("Hobbyene er:", self.skrivHobbyer())                                          #skriver ut en linje med hobbyene