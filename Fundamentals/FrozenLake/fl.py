from MDP.mdp import MDP
from GridEnv.gridenv import GridEnv
class FrozenLake(MDP, GridEnv):
    """
        A pygame environment for frozenlake is built using the characteristic
        of mdp.

    """
    def __init__(self):
        self.states = states
        self.rewards = rewards
        self.transitions = transitions
        self.actions = actions

if __name__ == "__main__":
    fl = FrozenLake()
    

