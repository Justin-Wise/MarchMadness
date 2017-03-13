from __future__ import division
import csv
from Game import Game


class Season:

	

	def __init__(self, y, tid):
		self.year = y
		self.id = tid
		self.games = []
		self.getGames()
	
	def getGames(self):
		with open('RegularSeasonDetailedResults.csv','rb') as theFile:
			reader = csv.DictReader(theFile)
			for line in reader:
				#print line
				if (self.year == int(line["Season"])):
					if (self.id == int(line['Wteam'])):
						game_data = line
						some_game = Game(**game_data)
						self.games.append(some_game)
					elif (self.id == int(line['Lteam'])):
						game_data = line
						some_game = Game(**game_data)
						self.games.append(some_game)
						

		
	
					

	def getScoringAverage(self):
		points = 0
		for x in range(0, len(self.games)):
			if (self.id == int(self.games[x].Wteam)):
				points = points + int(self.games[x].Wscore)
			elif (self.id == int(self.games[x].Lteam)):
				points = points + int(self.games[x].Lscore)

		return points/len(self.games)

	def getScoringDefenseAverage(self):
		points = 0
		for x in range(0, len(self.games)):
			if (self.id == int(self.games[x].Wteam)):
				points = points + int(self.games[x].Lscore)
			elif (self.id == int(self.games[x].Lteam)):
				points = points + int(self.games[x].Wscore)

		return points/len(self.games)

		

