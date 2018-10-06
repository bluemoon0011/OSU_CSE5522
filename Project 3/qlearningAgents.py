# qlearningAgents.py
# ------------------
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


from game import *
from learningAgents import ReinforcementAgent
from featureExtractors import *

import random,util,math

class QLearningAgent(ReinforcementAgent):
    """
      Q-Learning Agent

      Functions you should fill in:
        - computeValueFromQValues
        - computeActionFromQValues
        - getQValue
        - getAction
        - update

      Instance variables you have access to
        - self.epsilon (exploration prob)
        - self.alpha (learning rate)
        - self.discount (discount rate)

      Functions you should use
        - self.getLegalActions(state)
          which returns legal actions for a state
    """
    def __init__(self, **args):
        "You can initialize Q-values here..."
        ReinforcementAgent.__init__(self, **args)
        "*** YOUR CODE HERE ***"
        self.QValue=util.Counter() # define Q-value as Counter class


    def getQValue(self, state, action):
        '''
        desc:
          Returns Q(state,action)
          Should return 0.0 if we have never seen a state
          or the Q node value otherwise
        :param state: current state
        :param action: the action that the agent will take
        :return: Q-value Q(s,a)
        '''
        "*** YOUR CODE HERE ***"
        if not self.QValue.has_key((state,action)): # if Q-value doesn't have the that state and action, we will initialize the Q-value
            self.QValue[(state,action)]=0.0
        return self.QValue[(state,action)]


    def computeValueFromQValues(self, state):
        '''
        desc:
          Returns max_action Q(state,action)
          where the max is over legal actions.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return a value of 0.0.
        :param state: current state
        :return: the relationship between Value and Q-value is V(s)=max_a{Q(s,a)}
        '''
        "*** YOUR CODE HERE ***"
        QValue=util.Counter() # define a Counter class Q-value
        if len(self.getLegalActions(state))==0: # if current state cannot take any legal action, return 0 as value V(s)
            maxValue=0.0
        else: # otherwise
            for action in self.getLegalActions(state): # check all the legal actions
                QValue[action]=self.getQValue(state, action) # get a list of Q-value under current state and action
            maxValue = QValue[QValue.argMax()]# get the value V(s)=max_a{Q(s,a)}
        return maxValue

    def computeActionFromQValues(self, state):
        """
        desc:
          Compute the best action to take in a state.  Note that if there
          are no legal actions, which is the case at the terminal state,
          you should return None.
        :param state: current state
        :return: the best action that the agent can take at current state
        """
        "*** YOUR CODE HERE ***"
        QValue = util.Counter()
        if len(self.getLegalActions(state))==0:# if current state cannot take any legal action, return 0 as value V(s)
            bestAction=None
        else:
            for action in self.getLegalActions(state):# check all the legal actions
                QValue[action]=self.getQValue(state,action)# get a list of Q-value under current state and action
            bestAction=QValue.argMax()# the best action can be calculated by the argmax_a{Q(s,a)}
        return bestAction

    def getAction(self, state):
        """
        desc:
          Compute the action to take in the current state.  With
          probability self.epsilon, we should take a random action and
          take the best policy action otherwise.  Note that if there are
          no legal actions, which is the case at the terminal state, you
          should choose None as the action.

          HINT: You might want to use util.flipCoin(prob)
          HINT: To pick randomly from a list, use random.choice(list)
        :param state: current state
        :return: the best action of a random action
        """
        # Pick Action
        legalActions = self.getLegalActions(state)
        action = None
        "*** YOUR CODE HERE ***"
        if len(self.getLegalActions(state))==0:
            action=None
        else:
            if util.flipCoin(self.epsilon): # if the current random number < the  probability epsilon, the agent will act randomly
                action = random.choice(self.getLegalActions(state))
            else:# if the current random number < the  probability epsilon, the agent will act as the policy(best action)
                action = self.computeActionFromQValues(state)
        return action


    def update(self, state, action, nextState, reward):
        """
        desc:
          The parent class calls this to observe a
          state = action => nextState and reward transition.
          You should do your Q-Value update here

          NOTE: You should never call this function,
          it will be called on your behalf
        :param state: current state
        :param action: the action that the agent will take
        :param nextState: the next state after the agent take current action
        :param reward: the living reward
        :return: no return, but this function will update the Q-value the next episode.
        """
        "*** YOUR CODE HERE ***"
        sampleQValue=reward+self.discount*self.getValue(nextState)
        self.QValue[(state,action)]=(1-self.alpha)*self.getQValue(state,action)+self.alpha*sampleQValue


    def getPolicy(self, state):
        '''
        desc:
          To get the policy (best action)
        :param state: current state
        :return: the policy
        '''
        return self.computeActionFromQValues(state)

    def getValue(self, state):
        """
        desc:
          get value V(s)
        :param state: current state
        :return: V(s)
        """
        return self.computeValueFromQValues(state)


class PacmanQAgent(QLearningAgent):
    "Exactly the same as QLearningAgent, but with different default parameters"

    def __init__(self, epsilon=0.05,gamma=0.8,alpha=0.2, numTraining=0, **args):
        """
        These default parameters can be changed from the pacman.py command line.
        For example, to change the exploration rate, try:
            python pacman.py -p PacmanQLearningAgent -a epsilon=0.1

        alpha    - learning rate
        epsilon  - exploration rate
        gamma    - discount factor
        numTraining - number of training episodes, i.e. no learning after these many episodes
        """
        args['epsilon'] = epsilon
        args['gamma'] = gamma
        args['alpha'] = alpha
        args['numTraining'] = numTraining
        self.index = 0  # This is always Pacman
        QLearningAgent.__init__(self, **args)

    def getAction(self, state):
        """
        Simply calls the getAction method of QLearningAgent and then
        informs parent of action for Pacman.  Do not change or remove this
        method.
        """
        action = QLearningAgent.getAction(self,state)
        self.doAction(state,action)
        return action


class ApproximateQAgent(PacmanQAgent):
    """
       ApproximateQLearningAgent

       You should only have to overwrite getQValue
       and update.  All other QLearningAgent functions
       should work as is.
    """
    def __init__(self, extractor='IdentityExtractor', **args):
        self.featExtractor = util.lookup(extractor, globals())()
        PacmanQAgent.__init__(self, **args)
        self.weights = util.Counter()

    def getWeights(self):
        """
        desc: get the weights of agent
        :return: the weights
        """
        return self.weights

    def getQValue(self, state, action):
        """
        desc: get Q-value Q(s,a), Q(s,a)= sum{f(s,a)*w(s,a)}
        :param state: current state
        :param action: current action
        :return: the Q-value Q(s,a)
        """
        "*** YOUR CODE HERE ***"
        QValue=0.0
        Features=self.featExtractor.getFeatures(state, action)
        Weights=self.getWeights()
        for i in Features.keys():
            QValue=QValue+Features[i]*Weights[i]
        return QValue

    def update(self, state, action, nextState, reward):
        """
        desc: update the weight by minimizing error(w), wi(s,a)=wi(s,a)+alpha*difference*fi(s,a)
        :param state: current state
        :param action: current action
        :param nextState: next state
        :param reward: living reward
        :return: no return, just update the weight wi(s,a)
        """
        """
           Should update your weights based on transition
        """
        "*** YOUR CODE HERE ***"
        Features = self.featExtractor.getFeatures(state, action)
        Weights = self.getWeights()
        sampleQValue=reward + self.discount * self.getValue(nextState)
        difference=sampleQValue-self.getQValue(state, action)
        for i in Features.keys():
            Weights[i]=Weights[i]+self.alpha* difference * Features[i]

    def final(self, state):
        "Called at the end of each game."
        # call the super-class final method
        PacmanQAgent.final(self, state)

        # did we finish training?
        if self.episodesSoFar == self.numTraining:
            # you might want to print your weights here for debugging
            "*** YOUR CODE HERE ***"
            Weights=self.getWeights()
            for weight in Weights.keys():
                print "the value of weight %s is %f" % (str(weight), float(self.weights[weight]))
            pass
