from node import Node										#henter klassen Node
class Rack:													#klassenavn
	def __init__(self):										#konstruktør
		self._rack = []										#liste for noder

	def settInn(self, node):								#instansmetode med argument
		self._rack.append(node)								#legger til node til listen over node

	def getAntNoder(self):									#instansmetode
		return len(self._rack)								#returnerer lengden av listen med noder

	def antProsessorer(self):								#instansmetode
		antProsesser = 0									#variabel for å holde kontroll på antall prosesser
		for node in self._rack:								#løkke som itererer gjennom listen med noder
			antProsesser += node.antProsessorer()			#legger til antall prosesser som blir hentet fra nodeklassen
		return antProsesser									#returnerer totalt antall prosesser

	def noderMedNokMinneR(self, paakrevdMinne):				#instansmetode med ett argument
		antNoderMedNokMinne = 0								#variabel for å holde kontroll på antall noder med nok minne
		for node in self._rack:								#løkke som itererer gjennom listen med noder
			if node.nokMinne(paakrevdMinne):				#sjekker om noden har nok minne 
				antNoderMedNokMinne += 1					#hvis true legger den til en i teller variabelen 
		return antNoderMedNokMinne							#returnerer totalt antall noder med nok minne