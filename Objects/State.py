'''
Created on Nov 9, 2014

@author: Andrew
'''
from Parameters import game
import random
from Objects.Arrow import Arrow

class State(object):
    '''
    A single state, where one strategy is always played. Upon observing the opponents response, the state may lead to another state through its arrowlist
    '''

    def __init__(self, strategy):
        """
        A state should consist of a strategy, and by default will begin pointing to itself
        """
        self.strategy = strategy
        self.arrowList = []
    
    def randomStrategy(self):
        self.strategy = random.randint(0, len(game.payoffMatrix)-1)
                    
    def addRandomArrow(self, plan, arrowTarget=None, arrowCondition=None):
        newCondition = False
        while not newCondition:
            newCondition = True
            arrowCondition = []
            for player in range(0,game.numPlayers-1):
                arrowCondition.append(random.randint(0, len(game.payoffMatrix)-1))
            for arrow in self.arrowList:
                if arrowCondition == arrow.condition:
                    newCondition = False
        
        if arrowTarget is None:        
            arrowTarget = random.randint(0, len(plan.states)-1)    
        #For all but one player(themselves) a strategy is added to this list, upon which this arrow is conditioned
        randomArrow = Arrow(arrowTarget, arrowCondition)
        self.arrowList.append(randomArrow)