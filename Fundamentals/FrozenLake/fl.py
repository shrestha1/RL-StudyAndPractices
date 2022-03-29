import sys
import pygame
import time

from MDP.mdp import MDP
from GridEnv.gridenv import GridEnv

from utils import BLACK


class FrozenLake(MDP, GridEnv):
    """
        A pygame environment for frozenlake is built using the characteristic
        of mdp.

    """
    def __init__(self, states, actions, rewards, transitions, window_size, block_size):
        MDP.__init__(self, states, actions, rewards, transitions)
        GridEnv.__init__(self, window_size, block_size)



    def run(self):
        # global SCREEN, CLOCK
        pygame.init()
        CLOCK = pygame.time.Clock()
        while True:
            # print(state, action)
            self.SCREEN.fill(BLACK)
            self.draw()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    print("Exiting the game")
                    sys.exit()
            time.sleep(1)
            pygame.display.update()

