'''
Jobber med ordbøker hvor jeg legger til to nye varer og en pris inni ordboken min
'''
varer = {"melk":14.90, "brød":24.90, "yoghurt":12.90, "pizza":39.90}                #lager en ordbok med varer og pris
print(varer)                                                                        #skriver ut ordbok

varer[input("Legg til en varen: ")] = float(input("Hva koster den varen? "))        #legger til en pris og vare etterpå
varer[input("Legg til en varen: ")] = float(input("Hva koster den varen? "))        #legger til en pris og vare etterpå
print(varer)                                                                        #skriver ut denne ordboken på nytt
