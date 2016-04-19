'''
@author: Andrew
In order to prepare the simulation as desired, please go to the Parameters page, 
and change the inputs.
'''

from Parameters import parameters
from createPlayers import generateFirstGen, makeSets, birthGen, mutatePlayers
from PlayGame import playGame
from display import display
    
def main():
    individualList = generateFirstGen(parameters.numSets, parameters.startingStrategyDistribution)#Makes the first generation
        
    currentGen = 0#The current generation number
    while currentGen < parameters.numGenerations:#Plays the game for the number of generations specified
        currentGen += 1
        
        playerSetList = makeSets(individualList)#Groups players randomly to play together
         
        for playerSet in playerSetList:
            playGame(playerSet)#Players are put through the game, and get payoffs dependant upon their strategies

        individualList = birthGen(individualList)#Takes the payoffs of the old game and makes the new generation
        mutatePlayers(individualList)#Takes a new generation, and with some probability mutates players

    # diplay the resultant strategies 
    display(individualList)
    
    #make graph?
  
if __name__ == '__main__':
    main()
    
    
#AFTER GENERATION X Save actions played and then output average plays 