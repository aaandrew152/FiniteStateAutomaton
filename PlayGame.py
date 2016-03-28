import random
from Parameters import game

def playGame(playerSet):
    assert len(playerSet) == game.numPlayers
    
    gameOver = False
    assert game.probEnd < 1
    
    while not gameOver:
        gameOver = playRound(playerSet)
        #Continues playing the game until the game exits with probability probEnd
            
def playRound(playerSet):
    for player in playerSet:
        stratList = getStrategies(player, playerSet)
        player.payoff += nDimListAccess(stratList, game.payoffMatrix)
        player.plan.react(stratList)
    
    possibleEnd = random.random()
    if possibleEnd < game.probEnd:
        return True
    else:
        return False
       
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