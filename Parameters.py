'''
Created on Oct 29, 2014

@author: Andrew
'''
from Objects.Game import Game

class Parameters(object):
    '''
    Takes inputs from user
    '''
    def __init__(self):

        ## OVERALL SIMULATION PARAMETERS
        self.numSets = 100
        #input("How many sets(i.e. games played) per generation? This will be multiplied by the number of players in each game")
        self.numGenerations = 10000
        #input("How many generations?")
        self.collectGenerations = 100
        #input("How many generations from the end would you like the collect strategies played for?") Make 0 if not wanted. 
        assert(self.numGenerations > self.collectGenerations)
        self.numSims = 10
        #input("How many global simulations should be run?")
        

        # GAME SPECIFIC PARAMETERS
        self.mutationProb = 0.02
        #input("What is the chance of a mutation?")
        self.mutation_addState = 0.25
        self.mutation_deleteState = 0.25
        self.mutation_changeArrow = 0.25
        # self.mutation_changeAction = 1 - (previous probabilities)
        assert(self.mutation_addState + self.mutation_deleteState + self.mutation_changeArrow <= 1)


        self.startingStrategyDistribution = None
        #Set this equal to the distribution wished, ex) = [.5, .5] would state that half play either strategy
        self.discountFactor = .98
        #With what probability does the game repeat?
        self.payoffMatrix = (
                             (2, 0),
                             (3, 1)
                             )
        #This is an example of the payoff matrix for the Prisoners dilemma
        #Note that payoffs are symmetric, and only the first players values are entered.

        self.noise = False ## TO BE IMPLEMENTED
        # set to 'True' if you want to add noise to the system
        # specify amount of noise (false pos and false negs)

        self.mutationPrune = False
        # set to 'True' if you want to prune the strategy after any mutation occurs


        ## OUPUT PARAMETERS

        self.prevalence = 5
        # set the threshold prevalence for which strategies are saved 

        self.saveOutput = True
        # set to 'True' if you want to save the program's output to a file
        self.withGraphics = True
        # set to 'True' if you want to generate graphical representations of strategies 
        self.directory = 'test8/'
        # specify name of directory to save ouput into, 'simulations' by default

parameters = Parameters()
game = Game(parameters)
        