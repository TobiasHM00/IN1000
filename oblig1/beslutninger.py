'''
Her bruker jeg en if-sjekk for å sjekke et svar til hva brukeren skriver inn.
Også skrive det ut til terminalen men print.
'''
svar = input("Har du lyst på en brus? (ja/nei)")    #Lagrer en verdi brukeren skriver inn men prøver å vise brukeren til hva jeg er ute etter med teksten jeg skriver inni input funksjonen

if svar == "ja":                                    #Sjekker om svaret er ja
    print("Her har du en brus!")                    #Og skriver ut en passende melding til svaret med print
elif svar == "nei":                                 #Sjekker om svaret er nei
    print("Den er grei.")                           #Og skriver ut en passende melding til svaret med print
else:
    print("Det forstod jeg ikke helt.")             #Hvis verdien i variabelen er verken ja eller nei skriver jeg ut en passende melding med print
