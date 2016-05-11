'''
@author: Andrew
In order to prepare the simulation as desired, please go to the Parameters page, 
and change the inputs.
'''

from Parameters import parameters
from createPlayers import generateFirstGen, makeSets, birthGen, mutatePlayers
from PlayGame import playGame
from display import display
from progress.bar import Bar
    
def main():

    bar = Bar('Processing',max = parameters.numGenerations)

    individualList = generateFirstGen(parameters.numSets, parameters.startingStrategyDistribution)#Makes the first generation
        
    actionsPlayed = []

    for gen in range(parameters.numGenerations):#Plays the game for the number of generations specified
        
        playerSetList = makeSets(individualList)#Groups players randomly to play together
         
        for playerSet in playerSetList:
            gameMoves = playGame(playerSet, gen >= (parameters.numGenerations - parameters.collectGenerations))#Players are put through the game, and get payoffs dependant upon their strategies
            actionsPlayed += gameMoves

        individualList = birthGen(individualList)#Takes the payoffs of the old game and makes the new generation
        mutatePlayers(individualList)#Takes a new generation, and with some probability mutates players

        bar.next()
    # diplay the resultant strategies 
    display(individualList,actionsPlayed)
      
    bar.finish()
if __name__ == '__main__':
    main()