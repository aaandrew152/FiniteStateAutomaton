from Objects.Player import Player
import random
from Parameters import game, parameters
from Objects.Plan import Plan
import math

def birthGen(individualList):
    newIndividualList = []
    
    totalPayoff = 0
    for player in individualList:
        player.payoff = math.exp(player.payoff)#Exponentiate payoffs in order to normalize
        totalPayoff += player.payoff
        
    for _ in individualList:
        newPlayer = makePlayer(individualList, totalPayoff)
        newIndividualList.append(newPlayer)
        
    return newIndividualList
    '''
    I decided here not to use the birthing procedure used by Vanveelen which would involve the possibility
    of copying an individual every other individual, as I did not see the value in such a procedure(I'm willing
    to change this if requested).
    
    This method draws an individual from the list with probabilities scaled upon the different individuals payoffs
    After that the individual has a chance(determined in parameters) of mutating.
    '''
        
def makePlayer(individualList, totalPayoff):
    randomPayoff = random.uniform(0, totalPayoff)
    
    runningPayoffTotal = 0
    for player in individualList:
        runningPayoffTotal += player.payoff
        if runningPayoffTotal > randomPayoff:
            newPlayer = Player(player.plan)
            return newPlayer
                
def makeSets(individualList):
    playerSetList = []
    tempIndividualList = list(individualList)
    while tempIndividualList:
        playerSet = []
        for player in range (game.numPlayers):
            x = random.randint(0,len(tempIndividualList)-1)
            playerSet.append(tempIndividualList.pop(x))
        playerSetList.append(playerSet)
    return playerSetList

def generateFirstGen(numSets, startStrategyDistribution):
    numPeople = numSets * game.numPlayers
    indList = []
    if startStrategyDistribution is None:
        for _ in range(numPeople):
            indList.append(Player())
    else:
        assert sum(startStrategyDistribution) == 1
        
        for idx, strategy in enumerate(startStrategyDistribution):
            for newPlayer in range(int(strategy*numPeople)):
                indList.append(Player(Plan(idx)))
        
    return indList
    #Makes the first generation with all players using the starting strategy.

def mutatePlayers(individualList):
    for player in individualList:
        randomMutate = random.uniform(0,1)
        if randomMutate < parameters.mutationProb:
            specificMutation = random.uniform(0,1)
            if specificMutation < 1/4:
                player.plan.addRandomState()
            elif specificMutation < 2/4:
                player.plan.deleteRandomState()
            elif specificMutation < 3/4:
                player.plan.changeArrow()
            else:
                player.plan.changeStateStrat()
