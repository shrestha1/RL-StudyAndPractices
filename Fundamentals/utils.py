BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
BLUE = (0, 0, 200)
RED = (200, 0, 0)
GREEN = (0,125,0)

global walls_coordinate
walls_coordinate = {(3,0), (1, 2)}

global Goal_coordinate 
Goal_coordinate = (3,3)

actions = {"LEFT":(0,-1),"UP":(-1,0),"RIGHT":(0,1),"DOWN":(1,0)}

def g2c(coordinate:tuple, pixel_unit:int) -> tuple:
    """
        Convert pygame coordinate to cartesian coordinate. x pixel unit 
        refers to 1 unit in cartesian coordinate system. For example:
        if pixel unit is 100 then 100 pixel is one unit in cartesian system
    

    coordinate: game coordinate (x, y)
    pixel_unit: int


    return: tuple
    """
    return (int(x/pixel_unit), int(y/pixel_unit))

def c2g(coordinate:tuple, pixel_unit:int) -> tuple:
    """
        cartesian coordinate to pygame coordinate
    
    coordinate: cartesian coordinate (x, y)
    pixel_unit: int

    return: tuple
    """
    return (int(x*pixel_unit), int(y*pixel_unit))

def transitions(states, actions) -> dict:

    transitions = {state:{} for state in states}

    for state in states:
        for action in actions:
            count = 0.0
            # just sum = state + actions[action]
            # u_sum = [sum(x) for x in zip(state, actions[action])]
            result = tuple(( sum(x) for x in zip(state, actions[action]))  )        
            # transitions
            # print('state: ', state, ', action: ', actions[action], ', u_sum: ', u_sum, ', result', result)
            T = []
            if result in states:
                T.append(build_actions(result, 0.0))
                T.append(build_actions(state, 0.1))
                # for any action (if result in the state space) we increase count  
                count += 0.1  
            else:
                T.append(build_actions(state, 0.0)) 
                
            for a in actions:
                if (a != action):
                    result2 = tuple( (sum(x) for x in zip(state, actions[a])) ) 
                    #print('result2: ', result2, ', a: ', a, ', action: ', action)
                    if result2 in states:
                        count += 0.1
                        T.append(build_actions(result2, 0.1))
            T[0][0] = 1.0 - count
            
            transitions[state][action] = T
            # print('state: ', state, ', action: ', action, ', transitions: ', T)
    
    transitions[Goal_coordinate] = {"EXIT":[(0.0, Goal_coordinate)]}

    return transitions


def build_actions(state, prob) -> list:
    return[prob, state]

def rewards(states):
    reward = {state: -1 for state in states}

    #few states have particular reward
    for wall in walls_coordinate:
        reward[wall] = -10

    reward[Goal_coordinate] = +50
    return reward    

def states(window_size, block_size):
    return [(int(i/block_size), int(j/block_size)) for i in range(0, window_size[0], block_size) for j in range(0, window_size[1], block_size)]
