'''
Test program for sang.py som sender inn artist, tittel og lydfil. 
Spiller av lydfilen som ble sendt herifra
NB! Når du kjører dette programmet så vil sangene spilles av når de blir laget som objekt og i løkken som spiller alle sangen i listen
'''
from sangMedAudio import Sang                                           #henter sang klassen
def hoved():                                                            #hovedprogram i en prosedyre
    adagio = Sang("Albinoni", "Adagio", "adagio.wav")                   #nytt sangobjekt med tre parametere
    adagio.spill()                                                      #kaller på spill funksjonen med objektet
    odetojoy = Sang("Beethoven", "Ode to Joy", "ode_to_joy.wav")        #nytt sangobjekt med tre parametere
    odetojoy.spill()                                                    #kaller på spill funksjonen med objektet
    sangliste = []                                                      #liste for sangene
    sangliste.append(adagio)                                            #legger adagio sangen i listen
    sangliste.append(odetojoy)                                          #legger Ode to Joy sangen i listen
    for sang in sangliste:                                              #løkke som går gjennom listen
        sang.spill()                                                    #spiller den sangen som løkken fant også går videre
hoved()                                                                 #kaller hovedprogram