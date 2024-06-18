'''
Lag et program der brukeren blir quizet i hovedstader i Europa. Når brukeren svarer riktig skriv ut en passende melding også videre til neste spørsmål.
Gjør det samme hvis brukeren svarer feil. Når quizen er ferdig oppgi hvor mange rikgtige brukeren fikk. Lag 5 spørsmål selv.
'''
svar = input("Hva er hovedstaden til Spania? (bare små bokstaver) ")
tellriktige = 0

if svar == "madrid":
    print("Riktig svar!")
    tellriktige = tellriktige + 1
    svar = input("Hva er hovedstaden til Hellas? (bare små bokstaver) ")
else:
    print("Feil svar!")
    svar = input("Hva er hovedstaden til Hellas? (bare små bokstaver) ")

if svar == "athen":
    print("Riktig svar!")
    tellriktige = tellriktige + 1
    svar = input("Hva er hovedstaden til Finnland? (bare små bokstaver) ")
else:
    print("Feil svar!")
    svar = input("Hva er hovedstaden til Finnland? (bare små bokstaver) ")

if svar == "helsinki" or svar == "helsingfors":
    print("Riktig svar!")
    tellriktige = tellriktige + 1
    svar = input("Hva er hovedstaden til Ukrania? (bare små bokstaver) ")
else:
    print("Feil svar!")
    svar = input("Hva er hovedstaden til Ukrania? (bare små bokstaver) ")

if svar == "kiev":
    print("Riktig svar!")
    tellriktige = tellriktige + 1
    svar = input("Hva er hovedstaden til Estland? (bare små bokstaver) ")
else:
    print("Feil svar!")
    svar = input("Hva er hovedstaden til Estland? (bare små bokstaver) ")

if svar == "tallinn":
    print("Riktig svar!")
    tellriktige = tellriktige + 1
    print("Du fikk" , tellriktige, "av 5 riktige!")

    if tellriktige == 5:
        print("Du fikk full pott! Gratis!")
else:
    print("Feil svar!")
    print("Du fikk" , tellriktige, "av 5 riktige!")
