'''
Lag et program der brukeren kan skrive inn navnet på 5 venner i en liste og bursdagen deres i en annen liste.
Legg disse to listene inn i en ordbok ved hjelp av løkker, sånn at navn og bursdagsdato stemmer.
Skriv ut ordboken. Be så brukeren om et navn fra ordboken og sjekke om navnet er i ordboken og skriv ut bursdagsdatoen.
Hvis navnet ikke er i brukeren skriv en feilmelding.
'''
navn = []                                                                       #tom liste til navn
bursdag = []                                                                    #tom liste til bursdagsdatoer
dict = {}                                                                       #tom ordbok

for person in range(5):                                                         #kjører løkken 5 ganger
    navn.append(input("Skriv et navn: "))                                       #legger til et navn i navnelisten
    bursdag.append(input("Skriv en brusdagsdato (for eks. 25.sept): "))         #legger til en bursdagsdato til listen sin

for teller in range(len(navn)):                                                 #løkke som kjører sånn at navnen er nøkklene og bursdagsdatoene er elementene
    dict[navn[teller]] = bursdag[teller]

print(dict)                                                                     #skriver ut ordboken

velg = input("Skriv et navn du vil ha bursdagen til: ")                         #ber om et navn
if velg in dict:                                                                #sjekker om navnet er i ordlisten sine nøkkler
    print("Bursdagen til denne personen er: ", dict[velg])                      #skriver ut bursdagsdatoen
else:
    print("Kjenner ikke til dette navnet")                                      #feilmeldingen hvis navnet ikke er i ordboken
