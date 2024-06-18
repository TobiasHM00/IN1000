class Node:										#klassenavn
	def __init__(self, minne, antPros):			#konduktør med to argumenter
		self._minne = minne						#instansvariabel
		self._antPros = antPros					#instansvariabel

	def antProsessorer(self):					#instansmetode
			return self._antPros				#retunerere instansvariabel med ant prosesser

	def nokMinne(self, paakrevdMinne):			#instansmetode med ett argument
		if self._minne >= paakrevdMinne:		#sjekker om minne til noden er like mye eller mer enn det påkrevdeminne
			return True							#returnerer true
		return False							#returnerer false