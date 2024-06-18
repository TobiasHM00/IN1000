1   def print_prosa():
4,10     print("Melding til alle gaarderier:")
5,11     print("Antall dyr paa gaarden: ")

2   antall_dyr = 4
3   print_prosa()
6   print(antall_dyr)
7   antall_nye_dyr = int(input("Hvor mange nye dyr kommer til gaarden: "))
8   antall_dyr = antall_dyr + antall_nye_dyr
9   print_prosa()
12  print(antall_dyr)

13  if antall_dyr > 12:
        print("Det er mer enn ett dusin dyr paa gaarden!")
14  elif antall_dyr == 12:
15      print("Det er ett dusin dyr paa gaarden!")
    else:
        print("Det er mindre enn ett dusin dyr paa gaarden!")
