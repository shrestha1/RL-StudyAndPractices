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
        self.x, self.y = 0, 0
        self.dx, self.dy = 0, 0
        self.rect = pygame.rect.Rect((self.x*self.block_size, self.y*self.block_size, self.block_size, self.block_size))

    def draw(self, surface):
        pygame.draw.rect(surface, (self.x, self.y, 128), self.rect)


    def step(self,action):
        
        if action =="LEFT":
            self.dx, self.dy =  0, -1
            time.sleep(1)
        if action == "RIGHT":
            self.dx, self.dy = 0, 1
            time.sleep(1)
        if action == "UP":
            self.dx, self.dy = -1, 0
            time.sleep(1)
        if action =="DOWN":
            self.dx, self.dy = 1, 0
            time.sleep(1)
        
        self.x += self.dx
        self.y += self.dy

        self.rect = pygame.rect.Rect((self.x*self.block_size, self.y*self.block_size, self.block_size, self.block_size))
        self.dx, self.dy = 0, 0


    def run(self, policy):
        # global SCREEN, CLOCK
        pygame.init()
        CLOCK = pygame.time.Clock()
        while True:
            # print(state, action)
            self.SCREEN.fill(BLACK)
            self.draw_env()
            self.draw(self.SCREEN)
            
            self.step(policy[(self.x,self.y)])
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    print("Exiting the game")
                    sys.exit()
            time.sleep(1)
            pygame.display.update()

