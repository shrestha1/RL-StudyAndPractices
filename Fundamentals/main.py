from FrozenLake.fl import FrozenLake
from utils import actions, transitions, build_actions, rewards, states, walls_coordinate, Goal_coordinate
from algorithms import policy

WINDOW_COORDINATE = (400,400)
BLOCK_SIZE = 100

states = states(WINDOW_COORDINATE, BLOCK_SIZE)
transitions = transitions(states, actions)
rewards = rewards(states)

# Frozen Lake object
fl = FrozenLake(states, actions, rewards, transitions, WINDOW_COORDINATE,BLOCK_SIZE)
fl.set_goal(Goal_coordinate)
fl.set_walls(walls_coordinate)


if __name__ == "__main__":
    # Generate Policy using value iteration
    policy = policy(fl)

    # run the env using the policy
    fl.run(policy)
