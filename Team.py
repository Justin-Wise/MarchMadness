from Season import Season

class Team:
	

	
	def __init__(self,tid):
		self.id = tid
		self.seasons = []
		#self.getSeasons(2016,2016)
		self.getSeasons()

	def getSeasons(self):
		#for x in range(byear, endyear):
		self.seasons.append(Season(2016,self.id))
			
	

	
