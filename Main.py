from Team import Team
import Season
from Neural import NeuralNetwork
from numpy import exp, array, random, dot
import csv
def getTeamNames():
	teamList = []
	firstline = True;

	with open('Teams.csv','r') as f:
		reader = csv.reader(f)
		for row in reader:
			if firstline:
				firstline = False
				continue
			teamList.append(Team(row[1],row[0]))

		
	print "Team list generated"
	return teamList

def main():
	numgames = 0
	teamList = []
	for x in range(1101,1110):
		flag = True
		print x
		T = Team(x)
		for y in range(0,13):
			numgames = len(T.seasons[y].games)
			if (numgames == 0):
				print "false"
				flag = False
				continue
		if (flag == True):
			print "Added"
			teamList.append(T)
	#print teamList[4].seasons[0].getScoringAverage()




main()

#print tL[i].id



