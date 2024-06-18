from rack import Rack															#henter rack klassen
class Regneklynge:																#klassenavn
	def __init__(self, noderPerRack):											#konstruktør med ett argument
		self._noderPerRack = noderPerRack										#instansvariabel
		self._regneklynge = []													#liste som holder alle racksene

	def settInnNode(self, node):												#instansmetode med ett argument
		for rack in self._regneklynge:											#løkke som går gjennom listen med racks
			if rack.getAntNoder() < self._noderPerRack:							#sjekker om antall noder i racken er mindre enn maks antall noder som kan være i en rack
				rack.settInn(node)												#hvis der plass så setter den inn noden
				return None														#og avslutter metoden ved å returnere None
		nyrack = Rack()															#lager ett nytt rack objekt
		nyrack.settInn(node)													#setter inn noden i racken
		self._regneklynge.append(nyrack)										#legger til den nye racken til regneklyngen

	def antProsessorer(self):													#instansmetode
		antProsesser = 0														#variabel for å holde kontroll på antall prosesser
		for rack in self._regneklynge:											#løkke som itererer gjennom listen med noder
			antProsesser += rack.antProsessorer()								#legger til antall prosesser som blir hentet fra nodeklassen
		return antProsesser														#returnerer totalt antall prosesser

	def noderMedNokMinne(self, paakrevdMinne):									#instansmetode med ett argument
		antNoderMedNokMinne = 0													#variabel for å holde kontroll på antall noder fra rackene med nok minne
		for rack in self._regneklynge:											#løkke som itererer gjennom listen med racks
			antNoderMedNokMinne += rack.noderMedNokMinneR(paakrevdMinne)		#legger til antall noder med nok minner til i variabelen
		return antNoderMedNokMinne												#returnerer totalt antall noder med nok minne

	def antRacks(self):															#instansmetode
		return len(self._regneklynge)											#returnerer lengden på regneklynge listen