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
        self.numSets = 2
        #input("How many sets(i.e. games played) per generation? This will be multiplied by the number of players in each game")
        self.numGenerations = 100
        #input("How many generations?")
        self.mutationProb = .2
        #input("What is the chance of a mutation?")
        self.startingStrategyDistribution = None
        #Set this equal to the distribution wished, ex) = [.5, .5] would state that half play either strategy
        self.discountFactor = .5
        #With what probability does the game repeat?
        self.payoffMatrix = (
                             (2, 0),
                             (5, 1)
                             )
        #This is an example of the payoff matrix for the Prisoners dilemma
        #Note that payoffs are symmetric, and only the first players values are entered.

parameters = Parameters()
game = Game(parameters)
        