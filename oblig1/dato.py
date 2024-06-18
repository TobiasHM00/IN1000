'''
Dette programmet skal sjekke om datoene brukeren setter inn er enten i riktig rekkefølge, i feil rekkefølge eller sammme dato
tenkte først å sjekke om datoene er like men det ble veldig mange if-sjekker så da prøvde jeg å sjekke månedene først også datoen og det funket mye bedre
'''
dagen = input("Skriv en dato men uten månden og årstall: ")         #ber brukeren skrive inn en dato for å lagre verdien
maaneden = input("Skriv en måned som tall: ")                       #ber brukeren skrive inn en måned som tall til variabelen
dagto = input("Skriv en dato men uten månden og årstall: ")         #ber brukeren skrive inn enda en dato inn i variabelen
maanedto = input("Skriv en måned som tall: ")                       #ber brukeren skrive inn en måned som et tall til variabelen

if maaneden < maanedto:                                             #sjeker om maaneden er mindre enn maanedto
    print("Riktig rekkefølge!")                                     #hvis det er sant skriver programmet ut en riktig melding til sjekken
elif maaneden > maanedto:                                           #sjekker om maaneden er større enn maanedto
    print("Feil rekkefølge!")                                       #hvis det er sant skriver programmet ut en riktig melding til sjekken
else:                                                               #de to måndene kan være like og da må jeg sjekke hvilken dato som kommer først
    if dagen < dagto:                                               #sjekker om dagto er større enn dagen
        print("Riktig rekkefølge!")                                 #hvis det er sant kommer en tilsavrende melding
    elif dagen > dagto:                                             #sjekker om dagen er større en dagto
        print("Feil rekkefølge!")                                   #hvis det sant så kommer en tilsvarende melding
    else:                                                           #datoene kan også være helt like så da må vi sjekke det også
        print("Samme dato!")                                        #hvis det er sant kommer en passende melding
