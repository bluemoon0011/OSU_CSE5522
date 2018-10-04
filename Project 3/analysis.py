# analysis.py
# -----------
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


######################
# ANALYSIS QUESTIONS #
######################

# Set the given parameters to obtain the specified policies through
# value iteration.

def question2():
    answerDiscount = 0.9
    answerNoise = 0 # set noise to 0, the agent will never fall into the chasm
    return answerDiscount, answerNoise

def question3a():
    answerDiscount = 0.3
    answerNoise = 0 # set noise as 0, that the agent has probability to go into the cliff
    answerLivingReward = -0.7 # set answerLivingReward as negative value and its absolute value bigger then answerDiscount, which will make the agent prefer to go more shorter path
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3b():
    answerDiscount = 0.3
    answerNoise = 0.2 # set noise as positive value, which will give a huge penalty if the agent go into the cliff
    answerLivingReward = -0.7 # set answerLivingReward as negative value and its absolute value bigger then answerDiscount, which will make the agent prefer to go more shorter path
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3c():
    answerDiscount = 0.6
    answerNoise = 0 # set noise as 0, that the agent has probability to go into the cliff
    answerLivingReward = 0.2 # set answerLivingReward as positive value so the agent can get more reward if it choose to go on the longer path
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3d():
    answerDiscount = 0.6
    answerNoise = 0.2 # set noise as positive value, which will give a huge penalty if the agent go into the cliff
    answerLivingReward = 0.2 # set answerLivingReward as positive value so the agent can get more reward if it choose to go on the longer path
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3e():
    answerDiscount = 0.6
    answerNoise = 0.2 # set noise as positive value, which will give a huge penalty if the agent go into the cliff
    answerLivingReward = 20 # set answerLivingReward as very big positive value, so the agent will walk around to try its best to get living reward first
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question6():
    answerEpsilon = None
    answerLearningRate = None
    return answerEpsilon, answerLearningRate
    # If not possible, return 'NOT POSSIBLE'

if __name__ == '__main__':
    print 'Answers to analysis questions:'
    import analysis
    for q in [q for q in dir(analysis) if q.startswith('question')]:
        response = getattr(analysis, q)()
        print '  Question %s:\t%s' % (q, str(response))
