import random
import copy
from Parameters import game

def playGame(playerSet,collect):
    assert len(playerSet) == game.numPlayers
    
    gameOver = False
    assert game.probEnd < 1
    
    actionsPlayed = []

    while not gameOver:
        gameOver,actions = playRound(playerSet)
        if collect: 
            actionsPlayed += actions
        #Continues playing the game until the game exits with probability probEnd
    
    # return moves played in game
    return actionsPlayed
            
def playRound(playerSet):

    flag = True
    actions = []

    stratLists = [None]*len(playerSet)
            
    # for player in playerSet:
    #     stratList = getStrategies(player, playerSet)
    #     if flag:
    #         actions = copy.copy(stratList)
    #         flag = False
    #     player.payoff += nDimListAccess(stratList, game.payoffMatrix)
    #     player.plan.react(stratList) ##THIS MIGHT BE A PROBLEM

    for idx,player in enumerate(playerSet):
        stratList = getStrategies(player, playerSet)
        stratLists[idx] = stratList
        if flag:
            actions = copy.copy(stratList)
            flag = False
        player.payoff += nDimListAccess(stratList, game.payoffMatrix)
    
    for idx,player in enumerate(playerSet):
        player.plan.react(stratLists[idx]) ##THIS MIGHT BE A PROBLEM

    #print(strats)
    
    possibleEnd = random.random()
    if possibleEnd < game.probEnd:
        return True,actions
    else:
        return False,actions
    # return tuple with moves played
       
def nDimListAccess(accessList, matrix):
    if type(matrix) != int:
        element = accessList.pop(0)
        matrix = matrix[element]
        return nDimListAccess(accessList, matrix)
    else:
        return matrix
    
def getStrategies(player, playerSet):
    opposingPlayers = list(playerSet)
    opposingPlayers.remove(player)
    
    listOfStrat = [player.getCurrentStrat()]
    for player in opposingPlayers:
        listOfStrat.append(player.getCurrentStrat())
        
    return listOfStrat
    #Reorders the strategy list in order to bring the current players strategy to the front