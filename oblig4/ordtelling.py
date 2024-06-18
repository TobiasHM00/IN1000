'''
bruker to prosedyrer til å telle antall ord og hvor mange ganger ordet forekommer i setningen
'''
def ant_bokstaver(ord):
    return len(ord)

def ant_ord(setning):
    ordbok = {}
    ordene = setning.split()

    for ord in ordene:
        if ord in ordbok:
            ordbok[ord] += 1
        else:
            ordbok[ord] = 1
    return ordbok


setning = input("Skriv en setning: ")
print(ant_bokstaver(setning))
print(ant_ord(setning))
