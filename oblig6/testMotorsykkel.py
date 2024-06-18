from motorsykkel import Motorsykkel                                     #henter classen fra motorsykkel.py

def hovedprogram():                                                     #hoverdprogram porsedyre
    honda = Motorsykkel("Honda", "BR3456", 2348)                        #objekt
    bmw = Motorsykkel("BMW", "KT9736", 237)                             #objekt
    ducati = Motorsykkel("Ducati", "LV3284", 1482)                      #objekt

    honda.skrivUt()                                                     #skriver ut ojektet med infoen jeg sendte inn over
    bmw.skrivUt()                                                       #skriver ut ojektet med infoen jeg sendte inn over
    ducati.skrivUt()                                                    #skriver ut ojektet med infoen jeg sendte inn over

    ducati.kjor(10)                                                     #legger til 10 km på kilometertilstanden til ducati
    print("Kilometerstand:",ducati.hentKilometerstand())                #henter og skriver ut kilometertilstanden
hovedprogram()                                                          #kaller på prosedyren