'''
1.  Ja dette programmet vi kjøre så lenge brukeren skriver inn et heltall som er høyere eller lik 10.
    Man får bare ingen beskjeder for programmet har ingen spesifikasjoner på hva det skal gjøre med 10 eller høyere.

2.  Problemer som vil oppstå er når burkeren taster inn et tall som er under 10,
    fordi det er ikke mulig å plusse en string og et heltall, burde være ett komma istedenfor plusstegn
'''
a = input("Tast inn et heltall! ")
b = int(a)
if b < 10:
    print (b + "Hei!")
