class Game(object):
    '''
    This is where the game values are taken in for the game to be played
    '''


    def __init__(self, parameters):
        '''
        Takes in the payoff matrix for the game and uses it to construct the actions between players
        '''
        self.payoffMatrix = parameters.payoffMatrix
        self.numPlayers = len(self.payoffMatrix)#Number of columns of payoff matrix
        self.probEnd = parameters.discountFactor#Chance the game will end after a specific round
        