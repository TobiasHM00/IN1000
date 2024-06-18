from regneklynge import Regneklynge																				#henter regneklyngeklassen
from node import Node																							#henter node klassen
class Datasenter:																								#klassenavn
	def __init__(self):																							#konstruktør
		self._datasenter = {}																					#tom ordbok til alle regneklyngene

	def lesInnRegneklynge(self, filnavn): 																		#instansmetode med ett argument
		minfil = open(filnavn, "r")																				#åpner filen
		for linje in minfil:																					#løkke som går gjennom filen linje for linje
			linjeliste = linje.strip().split()																	#splitter hver linje og fjerner unødvendige tegn
			if len(linjeliste) == 1:																			#sjekker om listen av linjen er 1
				regneklynge = Regneklynge(int(linjeliste[0]))													#hvis listen er 1 lages det et nytt regneklynge objekt
			else:																								#hvis ikke
				for rack in range(int(linjeliste[0])):															#løkke som kjører antall ganger som det første elementet i linjelisten
					nynode = Node(int(linjeliste[1]),int(linjeliste[2]))										#lager ett nytt node objekt med det andre og tredje elementet i listen
					regneklynge.settInnNode(nynode)																#sender den nye noden til regneklynge klassen
		minfil.close()																							#lukker filen
		regneklyngenavn = filnavn.strip(".txt")																	#fjerner .txt fra filnavnet
		self._datasenter[regneklyngenavn] = regneklynge															#bruker det redigerte filnavnet som nøkkel og selve regneklypen som verdien til nøkkelen

	def skrivUtAlleRegneklynger(self):																			#instansmetode
		for regneklynge in self._datasenter:																	#løkke som kjører gjennom hver regneklynge i datasenteret
			print(f"Informasjon om regneklynge {regneklynge}:\n")												#utskrift av regneklynge navnet
			print(f"Antall rack: {self._datasenter[regneklynge].antRacks()}\n")									#utskrift av antall rack i regneklyngen
			print(f"Antall prosesser: {self._datasenter[regneklynge].antProsessorer()}\n")						#utskrift av totalt antall prosesser i regneklyngen
			print(f"Antall noder med minst 32GB: {self._datasenter[regneklynge].noderMedNokMinne(32)}\n")		#utskrift av totalt antall noder med 32GB minne
			print(f"Antall noder med minst 64GB: {self._datasenter[regneklynge].noderMedNokMinne(64)}\n")		#utskrift av totalt antall noder med 64GB minne
			print(f"Antall noder med minst 128GB: {self._datasenter[regneklynge].noderMedNokMinne(128)}\n")		#utskrift av totalt antall noder med 128GB minne

	def skrivUtRegneklynge(self, navn):																			#instansmetode med ett argument
		print(f"Informasjon om regneklynge {navn}:\n")															#utskrift av navnet til en valgt regneklynge
		print(f"Antall rack: {self._datasenter[navn].antRacks()}\n")											#antall racks i den utvalgte regneklyngen
		print(f"Antall prosesser: {self._datasenter[navn].antProsessorer()}\n")									#antall prosesser i den utvalgte regneklypen
		print(f"Antall noder med minst 32GB: {self._datasenter[navn].noderMedNokMinne(32)}\n")					#utskrift av totalt antall noder med 32GB minne i den utvalgte regneklyngen
		print(f"Antall noder med minst 64GB: {self._datasenter[navn].noderMedNokMinne(64)}\n")					#utskrift av totalt antall noder med 64GB minne i den utvalgte regneklyngen
		print(f"Antall noder med minst 128GB: {self._datasenter[navn].noderMedNokMinne(128)}\n")				#utskrift av totalt antall noder med 128GB minne i den utvalgte regneklyngen