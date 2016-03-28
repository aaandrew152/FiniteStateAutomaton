from Parameters import game
from Objects.State import State
import random
from Objects.Arrow import Arrow


class Plan(object):
    '''
    Here is where the strategy is replicated by a state machine
    '''

    def __init__(self, strategy):
        '''
        Takes in the index where the strategy is in order to decide the first strategy
        '''
        assert strategy in range(len(game.payoffMatrix))
        
        self.states = [State(strategy)]
        self.currentState = 0
    
    def react(self, listOfStrategies):
        for arrow in self.states[self.currentState].arrowList:
            if arrow.condition == listOfStrategies[1:]:
                self.currentState = arrow.target
            
    def getCurrentStrat(self):
        return self.states[self.currentState].strategy
    
    def addRandomState(self):
        randomStateStrategy = random.randint(0, len(game.payoffMatrix)-1)
        self.states.append(State(randomStateStrategy))
        
        allArrows = []
        for state in self.states:
            allArrows.extend(state.arrowList)
            
        if allArrows:
            arrowToChange = random.randint(0, len(allArrows)-1)
            currentArrow = 0
            for state in self.states:
                for arrow in state.arrowList:
                    if currentArrow == arrowToChange:
                        arrow.target = len(self.states)-1
                        return
                    else:
                        currentArrow += 1
        else:
            randomState = random.randint(0, len(self.states)-1)
            self.states[randomState].addRandomArrow(self, arrowTarget=len(self.states)-1)
                
    def deleteRandomState(self):
        if len(self.states) == 1:
            return
        else:
            stateToDelete = random.choice(self.states)
            
            for state in self.states:
                for arrow in state.arrowList:
                    while arrow.target == stateToDelete:
                        arrow.target = random.choice(self.states)
                        
            self.states.remove(stateToDelete)
            
    def changeArrow(self):
        stateToChange = random.randint(0, len(self.states)-1)
        totalPossibleArrows = (game.numPlayers-1)*(len(game.payoffMatrix))
        
        arrowToChange = random.randint(0, totalPossibleArrows-1)
        
        if arrowToChange < len(self.states[stateToChange].arrowList):
            self.states[stateToChange].arrowList[arrowToChange].target = random.choice(self.states)
        else:
            self.states[stateToChange].addRandomArrow(self)
            
    def changeStateStrat(self):
        stateToChange = random.randint(0, len(self.states)-1)
        
        self.states[stateToChange].randomStrategy()

    def stratNumbers(self):
        stratNumberList = [0 for x in range(len(game.payoffMatrix))]

        for idx, strat in enumerate(game.payoffMatrix):
            for state in self.states:
                if state.strategy == idx:
                    stratNumberList[idx] += 1
        return stratNumberList
        
        
        
            
        
            
        
            

        