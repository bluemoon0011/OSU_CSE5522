# valueIterationAgents.py
# -----------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


import mdp, util

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        '''
        desc:
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)

        :param mdp: mdp class
        :param discount: discount rate
        :param iterations: number of iterations
        '''

        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0

        # Write value iteration code here
        "*** YOUR CODE HERE ***"
        for k in range(self.iterations): # number of iterations < the given # of iterations.
            nextValues=util.Counter()
            for currentState in self.mdp.getStates(): # check all current states
                if self.mdp.isTerminal(currentState): # if currentState is terminal, then the next value of state will be 0.
                    nextValues[currentState]=0
                else:
                    maxQValue=float("-inf") # initialize the maxValue as -inf.
                    for action in self.mdp.getPossibleActions(currentState): # check all the possible actions that current state can take.
                        nextQValue=self.computeQValueFromValues(currentState,action) # get the max{maxValue, nextQValue}
                        maxQValue=max(nextQValue,maxQValue)# update max Q-value
                    nextValues[currentState]=maxQValue
            self.values=nextValues

    def getValue(self, state):
        '''
        desc:  get the value of current state
        :param state: current state
        :return: the value of the state (computed in __init__).
        '''

        return self.values[state]


    def computeQValueFromValues(self, state, action):
        '''
        desc:
          Compute the Q-value of action in state from the
          value function stored in self.values.
        :param state:
        :param action:
        :return:
        '''
        "*** YOUR CODE HERE ***"

        QValue=0
        for (nextState,transaction) in self.mdp.getTransitionStatesAndProbs(state, action):#get transaction probability and next state
            reward=self.mdp.getReward(state,action,nextState) # get reward: R(s,a,s')
            gamma=self.discount # get the discount parameter
            nextstateValue=self.getValue(nextState) # get V(s') value
            QValue=QValue+transaction*(reward+gamma*nextstateValue)#accumulate the value of all next states.
        return QValue

    def computeActionFromValues(self, state):
        '''
        desc:
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        :param state: current state
        :return: the policy (optimal action) for current state
        '''
        "*** YOUR CODE HERE ***"
        QValues= util.Counter()
        policy = None # if state is the terminal state, we won't change policy and this function will return None for policy
        if not self.mdp.isTerminal(state): # if the state is the terminal state, return the policy as None
            for action in self.mdp.getPossibleActions(state): # check all the actions
                QValues[action]=self.getQValue(state,action)# compute the Q-Value for all actions
            policy=QValues.argMax() # the policy should be the action with the max Q-value
        return  policy

    def getPolicy(self, state):
        '''
        desc: get the policy (optimal action) you want
        :param state: the current state
        :return: the policy that current state should take
        '''
        return self.computeActionFromValues(state)

    def getAction(self, state):
        '''
        desc: Returns the policy at the state (no exploration).
        :param state: current state
        :return: the optimal action for current state
        '''
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        '''
        desc: calculate the Q-value for current state and action
        :param state: current state
        :param action: the action that you will take
        :return: Q-value
        '''
        return self.computeQValueFromValues(state, action)
