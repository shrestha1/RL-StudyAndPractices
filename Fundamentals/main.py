from FrozenLake.fl import FrozenLake
from utils import actions, transitions, build_actions, rewards, states, walls_coordinate, Goal_coordinate

WINDOW_COORDINATE = (400,400)
BLOCK_SIZE = 100

states = states(WINDOW_COORDINATE, BLOCK_SIZE)
transitions = transitions(states, actions)
rewards = rewards(states)

fl = FrozenLake(states, actions, rewards, transitions, WINDOW_COORDINATE,BLOCK_SIZE)
fl.set_goal(Goal_coordinate)
fl.set_walls(walls_coordinate)
fl.run()
