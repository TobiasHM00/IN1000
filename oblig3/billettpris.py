'''
Her bruker vo en prosedyre for si hvor my en kunde skal betale for en billett
Kommentar til 5.
Ja det vil komme en feil hvis man følger oppgaven som den står.
Hvis man sjekker om alderen er høyere enn 17 så vil man hoppe over den siste linjen i if-sjekken som gir en discount til pensjonister.
Dette er en logisk feil og man burde sjekke om alderen er 17 eller yngre og 63 eller eldre.
Så kan man bruke else for å se no hvis alderen ikke er en av de to sjekkene.
'''
def billett():                                                          #definerer en prosedyre
    alder = int(input("Hva er alderen på kjøperen? "))                  #ber brukeren skrive inn en alder og lagrer den i en variabel
    billettpris = 0                                                     #lager en tom variabel fot

    if alder <= 17:                                                     #sjekker om alderen er 17 eller yngre
        billettpris = 30                                                #hvis true skal variabel billettpris ha prisen 30
    elif alder >= 63:                                                   #sjekker om alderen er 63 eller eldre
        billettpris = 35                                                #hvis true skal billettpris ha prisen 35
    else:                                                               #hvis alderen er ingen av de over sjekker jeg det
        billettpris = 50                                                #hvis true gir jeg billettpris prisen 50

    print("Du må betale", billettpris, "kr")                            #skriver ut en passende melding med prisen

billett()                                                               #kaller på prosedyren
