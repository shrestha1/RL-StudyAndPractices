import pygame
from utils import BLACK, GREEN, WHITE, RED

class GridEnv:
    def __init__(self,window_size:tuple, block_size:int):
        self.WINDOW_WIDTH, self.WINDOW_HEIGHT =  window_size
        self.block_size = block_size
        self.walls:list
        self.goal:tuple

        self.SCREEN = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))

    def draw_grid(self):
        for x in range(0, self.WINDOW_WIDTH, self.block_size):
            for y in range(0, self.WINDOW_HEIGHT, self.block_size):
                rect = pygame.Rect(x,y, self.block_size, self.block_size)
                pygame.draw.rect(self.SCREEN, WHITE, rect, 1)

    def get_walls(self):
        return self.walls
    
    def set_walls(self, walls):
        self.walls = walls

    
    def get_goal(self):
        return self.goal
    
    def set_goal(self, goal):
        self.goal = goal

    
    def draw_walls(self):
        for wall in self.walls:    
            rect = pygame.Rect(wall[0]*self.block_size,wall[1]*self.block_size, self.block_size, self.block_size)
            pygame.draw.rect(self.SCREEN, RED, rect)
    
    def draw_goal(self):
        
        rect = pygame.Rect(self.goal[0]*self.block_size,self.goal[1]*self.block_size, self.block_size, self.block_size)
        pygame.draw.rect(self.SCREEN, GREEN, rect)

    def draw(self):
        self.draw_grid()
        self.draw_walls()
        self.draw_goal()



def main():
    # global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((400, 400))
    CLOCK = pygame.time.Clock()
    while True:
        # print(state, action)
        SCREEN.fill(BLACK)
        env.draw()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                print("Exiting the game")
                sys.exit()
        time.sleep(1)
        pygame.display.update()

if __name__ == '__main__':
    walls_coordinate ={(3,0), (1, 2)}
    Goal_coordinate = (3,3)

    env = GridEnv((400,400),100)
    
    env.set_walls(walls_coordinate)
    env.set_goal(Goal_coordinate)
    main()