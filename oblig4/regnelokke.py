'''
Her så bruker vi løkker og lister til å skrive ut listen med tall og finner største og minste tall
Bruker float for står ikke noe i oppgaven om at det skal være heltall så da kan det være flyttall også
'''
tallListe = []                                              #definerer en tom liste for tallene
tall = float(input("Skriv et tall: "))                      #ber brukeren om ett tall
tallListe.append(tall)                                      #setter dette tallet inn i listen

while tall > 0:                                             #så lenge tallet er større enn null
    tall = float(input("Skriv et tall: "))                  #skal brukeren bli spurte om et nytt tall
    tallListe.append(tall)                                  #og skriver dette tallet inn i listen

tallListe.pop()                                             #vil ikke ha med 0 i listen så skriver den ut og kan bruke pop fordi løkken er ferdig når 0 blir skrevet
for tall in tallListe:                                      #går gjennom talllisten
    print(tall)                                             #skriver ut hvert element i listen

minSum = 0                                                  #variabel for summen

for tall in tallListe:                                      #løkke som går gjennom tallisten
    minSum += tall                                          #og legger sammen alle tallene i listen

print("Summen av disse tallene er", minSum)                 #skriver ut summen

storst = tallListe[0]                                       #variabel for største tall og setter den lik første elementet i listen
for indeks in range(len(tallListe)):                        #løkke som går gjennom listen
    if tallListe[indeks] > storst:                          #sjekker om tallet som blir sjekket er større enn det som står i størst variabelen
        storst = tallListe[indeks]                          #hvis det er sånn bytter vi verdien til den nye tall veriden

print("Det største tallet er", storst)                      #skriver ut den største tallverdien

minst = tallListe[0]                                        #variabel for minste tall og setter den lik første element i listen
for indeks in range(len(tallListe)):                        #løkke som går gjennom listen
    if  minst > tallListe[indeks]:                          #sjekker om tallet som blir sjekket er mindre enn det som står i minst variabelen
        minst = tallListe[indeks]                           #erstatter verdien hvis det er sant

print("Det minste tallet er", minst)                        #skriver ut den minste verdien
