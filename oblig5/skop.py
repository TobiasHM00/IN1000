'''
Det som skjer i dette programmet er at de to prosedyrene først bli definert. Så begynner programmet å kjøre med et kall på hovedprosedyren.
Den vil definere variabel a og b med de gitte verdeine, før den skriver ut b, så setter det vil den definere variabel b = a før den hopper opp til første prosedyre.
Der vil den gå gjennom løkken ved å sette c = 2 så skrive ut c før c blir økt med 1 og b = 10.
Programmet vil prøve å gjøre b = b + a men siden a ikke er en definert variabel inni denne prosedyren eller i de globale skopet vil det komme feilmelding om at a ikke er definert.
Så programmet vil slutte å kjøre.

Programmet kjørte som jeg trodde og skrev ut en feilmelding.
'''
def minFunksjon():
    for x in range(2):
        c = 2
        print(c)
        c += 1
        b = 10
        b += a
        print(b)
    return(b)

def hovedprogram():
    a = 42
    b = 0
    print(b)
    b = a
    a = minFunksjon()
    print (b)
    print (a)

hovedprogram()