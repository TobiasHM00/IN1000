'''Skriv en klasse Person med en konstruktør som tar imot navn og alder og oppretter
og initialiserer instansvariabler med disse. I tillegg skal konstruktøren opprette en
instansvariabel hobbyer som en tom liste . Skriv en metode leggTilHobby som tar
imot en tekststreng og legger den til i hobbyer-listen. Skriv også en metode
skrivHobbyer. Denne metoden skal skrive alle hobbyene etter hverandre på en linje.
Gi deretter Person-klassen en metode skrivUt som i tillegg til å skrive ut navn og
alder kaller på metoden skrivHobbyer.
Lag deretter et testprogram for klassen Person der du lar brukeren skrive inn navn og
alder, og oppretter et Person-objekt med informasjonen du får. Deretter skal brukeren
ved hjelp av en løkke få legge til så mange hobbyer de vil. Når brukeren ikke lenger
ønsker å oppgi hobbyer skal informasjon om brukeren skrives ut.'''

from person import Person                                                                           #henter klassen fra person.py
def hovedprogam():                                                                                  #definerer et hovedprogram
    navn = input("Skriv et navn: ")                                                                 #variabel med brukerinput for navn
    alder = input("Skriv en alder: ")                                                               #variabel med brukerinput for alder, gidder ikke skrive om alder til heltall for trenger den ikke som et tall i programmet, ville nok gjort det på eksamen for å vise kunnskapen
    pers1 = Person(navn, alder)                                                                     #sender navn og alder til person klassen
    inp = input("Skriv 'legg' for å legge til hobby eller trykk enter for å avslutte: ")            #inp for å styre programmet videre
    while inp == "legg":                                                                            #løkke som kjører så lenge inp er 'legg'
        pers1.leggTilHobby(input("Legg til en hobby: "))                                            #kaller på leggTilHobby med brukerinput for å legge til hobby
        inp = input("Skriv 'legg' for å legge til hobby eller trykk enter for å avslutte: ")        #ny verdi for inp variabelen
    pers1.skrivUt()                                                                                 #kaller på metoden skrivUt for å skrive ut info om personen
hovedprogam()                                                                                       #kaller på hovedprogram