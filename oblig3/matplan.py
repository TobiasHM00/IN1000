'''
Samler beboere i en ordbok sammen med matplanen deres en gitt dag. Bruker denne til å skrive ut hvilken beboer brukern vil se matplanen til
'''
#matplan1 = {"forkost":"pannekaker", "lunsj":"brødskiver", "middag":"kjøttkaker"}
#matplan2 = {"forkost":"bacon", "lunsj":"egg", "middag":"pølser"}
#matplan3 = {"frokost":"rundstykker", "lunsj":"fisk", "middag":"sushi"}
beboere = {"Per Persen":{"forkost":"pannekaker", "lunsj":"brødskiver", "middag":"kjøttkaker"},      #ordbok med tre beboere og deres matplan
           "Kari Nordmann":{"forkost":"bacon", "lunsj":"egg", "middag":"pølser"},
           "Karl Karlson":{"frokost":"rundstykker", "lunsj":"fisk", "middag":"sushi"}}

def pros():                                                                                         #definere en prosedyre
    print(beboere.keys())                                                                           #skriver ut nøkkel veridene til ordboken
    navn = input("Skriv navnet på beboeren du vil se matplanen for: ")                              #spør brukeren om et navn og lagrer det i en variabel
    if navn in beboere:                                                                             #sjekker om beboeren er i ordboken
        print(beboere[navn])                                                                        #hvis beboeren er det skrive rjeg ut matplanen til beboeren
    else:                                                                                           #hvis ikke må jeg også sjekke
        print("Denne beboeren finnes ikke ved dette sykhjemmet")                                    #skriver ut hvis beboeren ikke er registrert i ordboken

pros()                                                                                              #kaller på prosedyren

'''
Oppgave 3
a)Jeg ville brukt liste for alle brukernavnene men hvis jeg skulle koblet brukernavnene til en person ville jeg brukt ordboken

b)For brukernavn og poeng ville jeg brukt en ordbok og hvis jeg ville så kunne jeg ha utvidet og lagt til navn og annen info til personen

c)Ville brukt mengder for da kunne jeg sett vinnerne og hvis samme person hadde vunnet to ganger så slapp jeg å få navnet hans to ganger
    Hvis jeg skulle ha telt hvor mange ganger noen hadde vunnet så trenger jeg alle vinnere uansett om de har vunnet før så da hadde en liste vært best

d)Ordbok ville vært best her for du skal lagre allergier til matretter
'''
