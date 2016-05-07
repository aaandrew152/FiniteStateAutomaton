from random import randint
from Objects.Plan import Plan
from Parameters import game

class Player(object):
    '''
    A single person who is in the game with their strategies
    '''

    def __init__(self, plan=None):
        '''
        Sets up a player with the default strategy or a random strategy if none is provided
        '''
        if plan is None:
            self.plan = Plan(randint(0, len(game.payoffMatrix)-1))
        else:
            plan.currentState = 0
            self.plan = plan
        self.payoff = 0
        
    def toString(self):
        print("Player: ")
        for index,state in enumerate(self.plan.states):
            print ("State: " + str(index) + " is " + str(state.plan))
            
    def getCurrentStrat(self):
        return self.plan.getCurrentStrat()

    def getStratNumbers(self):
        return self.plan.stratNumbers()
    
    def __str__ (self):
        return "Strategy: " + str(self.getStratNumbers()) 
    #PRINT AVERAGE STRATEGY played last game?
            
    #Should consider arrows in current state as well as the moves made by others, and update strategy accordingly
