from Team import Team
import Season

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
	teamList = []
	for x in range(1001,1464):
		print x
		teamList.append(Team(x))
	print teamList[4].seasons[0].getScoringAverage()
main()

#print tL[i].id



