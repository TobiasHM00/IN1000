from hund import Hund                   #henter klasse
def hovedprogram():                     #definerer hovedprogram
    dog = Hund(4,7)                     #lager et objekt
    dog.spring()                        #kaller på spring metoden i klassen
    print(dog.hentVekt(), "kg")         #skriver ut vekten
    dog.spring()                        #kaller spring metoden
    print(dog.hentVekt(), "kg")         #skriver ut vekten
    dog.spis(4)                         #kaller spis metoden med 4
    print(dog.hentVekt(), "kg")         #skriver ut vekten
    dog.spring()                        #kaller spring metoden
    print(dog.hentVekt(), "kg")         #skriver ut vekten
    dog.spring()                        #kaller spring metoden
    print(dog.hentVekt(), "kg")         #skriver ut vekten
    dog.spis(2)                         #kaller spis metoden
    print(dog.hentVekt(), "kg")         #skriver ut vekten
hovedprogram()                          #kaller hovedprogram