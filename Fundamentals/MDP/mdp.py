# pylint: disable=missing-module-docstring
class MDP:
    '''
        Markov Decision Process
    '''
    def __init__(self, states, actions, rewards, transitions) -> None:
        '''
        '''
        self.states = states
        self.actions = actions
        self.rewards = rewards
        self.transitions = transitions

    def get_actions(self, state):
        '''
            Available actions in particular state
        '''
        return self.transitions[state].keys()

    def get_rewards(self, state):
        '''
            Reward
        '''
        return self.rewards[state]

    def get_transitons(self, state, action):
        '''
            Transition
        '''
        return self.transitions[state][action]
