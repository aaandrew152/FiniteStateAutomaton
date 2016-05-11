from Parameters import parameters
from createPlayers import generateFirstGen, makeSets, birthGen, mutatePlayers
from PlayGame import playGame
from display import display
import os
from progress.bar import Bar
    
def main():

	bar = Bar('Processing',max = parameters.numSims*parameters.numGenerations)
   	## RUN SIMULATIONS
	for sim in range(parameters.numSims):

	    individualList = generateFirstGen(parameters.numSets, parameters.startingStrategyDistribution)#Makes the first generation
	        
	    stratsPlayed = []

	    for gen in range(parameters.numGenerations):#Plays the game for the number of generations specified
	        
	        playerSetList = makeSets(individualList)#Groups players randomly to play together
	         
	        for playerSet in playerSetList:
	            gameMoves = playGame(playerSet, gen > (parameters.numGenerations - parameters.collectGenerations))#Players are put through the game, and get payoffs dependant upon their strategies
	            stratsPlayed += gameMoves

	        individualList = birthGen(individualList)#Takes the payoffs of the old game and makes the new generation
	        mutatePlayers(individualList)#Takes a new generation, and with some probability mutates players

	        bar.next()
	    # diplay the resultant strategies 
	    display(individualList,stratsPlayed,sim)
      
	bar.finish()

if __name__ == '__main__':
    main()