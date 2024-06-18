'''
Her skal vi omgjøre en temperatur fra fahrenheit til celsius
'''
tempFar = float(input("Oppgi en temperatur i faharenheit: "))       #får brukeren til å gi meg en temperatur i fahrenheit
print(tempFar, "F")                                                 #skriver ut denne temperaturen
tempCels = (tempFar - 32) * 5/9                                     #bruker formelen til å konvertere temperaturen til celsius
print(tempCels, "C")                                                #skriver ut temperaturen i celsius
