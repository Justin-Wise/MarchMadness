from Season import Season

class Team:
	

	
	def __init__(self,tid):
		self.id = tid
		self.seasons = []
		self.getSeasons(2003,2016)
		#self.getSeasons()

	def getSeasons(self,byear,endyear):
		for x in range(byear, endyear):
			self.seasons.append(Season(x,self.id))
			
	

	
