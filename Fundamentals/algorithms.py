def value_iteration(env):
    states = env.states
    # actions = env.actions
    
    # T and R are just short names for functions get_transition and get_rewards
    T = env.transitions
    R = env.rewards
        
    gamma = 0.9
    ep = 0.00001
    
    #initialize value of all the states to 0 (this is k=0 case)
    V1 = {s: 0 for s in states}
#    V1 = {s:0 for s in states}

    j = {s: 0 for s in states}
    while True:
        V = V1.copy()
        delta = 0
        
        # Bellman Equation, update the utility values
        # 
        for s in states:

            V1[s] = R[s] + gamma * max ([ sum([p * V[s1] for (p, s1) in T[s][a]]) for a in T[s].keys()])
            delta = max(delta, abs(V1[s] - V[s]))
            j[s] += 1
            
            
            # if (j[s]%5 == 0):
            # print('state: ', s, ', j: ', j[s])
        
        if (delta < ep):
            # for s in states:
            #     print('state: ', s, ', j: ', j[s])
            # print(iteration)
            return V        


def policy(env):
    states= env.states
    actions= env.actions
    T = env.transitions
    V = value_iteration(env)
    
    print(V)
    P={}
    for s in states:
        P[s] = max(T[s].keys(),  key= lambda a:sum([p*V[s1]  for (p,s1) in T[s][a]]))
        print(s,P[s])
    return P

