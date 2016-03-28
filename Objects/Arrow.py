'''
Created on Nov 18, 2014

@author: Andrew
'''
from Parameters import game

class Arrow(object):
    '''
    An arrow with two parts:
    First a condition which decides when it is activated
    Second a pointer, which 'states'(ha!) which target it targets.
    '''


    def __init__(self, target, condition):
        '''
        Arrow is  pointing to the target, and will trigger when condition is met
        '''
        self.target = target
        self.condition = condition
            
        