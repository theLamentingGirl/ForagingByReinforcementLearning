#%%
import numpy as np
import matplotlib.pyplot as plt

# State 0 == Mimic prey, State 1 == Model prey
alpha = 0.3 # Learning rate
gamma = 0.5 # Discount Factor
d0 = 3 # Constant for toxicity rejection function
epsilon = 10**-15 # Very small constant to check if learning is done

#HELPER FUNCTIONS
def dFunc(t):
    '''probability of rejecting a model based on taste sampling
    Returns: d(const)
    '''
    return 1-(1/(1+d0*t))

def rFunc(action, p, sampling, t):    
    ''' Reward - what's the reward for a choice at this time point. Depends on :
    action(boolean) - choosing non-toxic = 0 or toxic(mimic/actual) prey = 1
    p(const)- population of mimics(not actually toxic)
    t(const)- toxicity
    d(func)- 0 if no toxicity
    tasteSampling(boolean): 0 is no sampling; 1 if sampling

    Returns: R(const)
    '''

    if(action): 
        if sampling:
            d = dFunc(t)
            scale = 1/(1-(1-p)*d)
            return 2*p*scale +(1-t*t)*(1-p)*(1-d)*scale
        else:
            return 2*p+(1-t*t)*(1-p)
    else: return 1

#POLICY 
def pi(Q, s, a):
    '''
    Policy - the prob of attacking or not
    Q(numpy matrix): matrix size(state x action) Q-table. (here - 1x2 matrix)
    s(integer): -  state - initial state of predator. 0 if it not at all toxicity aversive
    a: action(boolean)
    return([0,1])prob - probabilty using soft-max policy 
    '''

    target = Q[s,a] 
    return np.exp(target)/sum([np.exp(Q[s,a]) for a in [0, 1]])

def pickAction(Q, s):
    '''
    Pick which action the predator performs using the softmax policy.
    return(boolean) - action
    '''
    prob0 = pi(Q, 0 , 0)    
    prob1 = 1-prob0 # There are only 2 actions
    return np.random.choice(2, 1, p = [prob0, prob1] )[0]

#ALGORITHM
def runQLearning(action, pop, toxicity, sampling):
    '''Run algorithm till the while loop condition stops - when the predator finishes learning. i.e. it has toxicity aversion.
    params: action, pop, tox, sampling
    returns: Q-table(numpy matrix) with the Q values are rewards along with long term future consideration
    ''' 

    R = np.array([[rFunc(0,pop,sampling, toxicity), rFunc(1,pop,sampling, toxicity)]])
    Q = np.zeros_like(R)
    A = [0,1]
    target = 800 # arbitrarily large error 
    
    while(abs(target - Q[0, action]) > epsilon):
        action = pickAction(Q, 0)
        Q_ = [Q[0,a] for a in A]
        maxQ = max(Q_)
        target = R[0, action] + gamma * maxQ # Reward of subsequent action plus discounted future reward
        TDError = alpha*(target - Q[0, action])
               
        Q[0, action] = Q[0, action] + TDError
               
    return Q

# CALCULATE POLICY
def calcPi(T_range, p_range, sampling):
    '''
    calculate the prob of attacking after running Q learning algo
    T-range(list): different values of toxicity
    p-range(list): prob of attacking
    sampling(bool)
    return: Z prob of toxic aversiveness
    '''

    X, Y = np.meshgrid(T_range, p_range)
    Z = np.zeros_like(X)
    
    interval = len(T_range)/10 # Use to print info about status of training
    count = 0
    
    for tIndex, t in enumerate(T_range):
        if(tIndex % interval <1): 
            print (str(count)+"0% Done")
            count+=1
        for pIndex, p in enumerate(p_range):
            Z[pIndex, tIndex] = pi(runQLearning(0, p, t, sampling),0,1)
    return Z

# PLOTTING CONTOUR PLOTS 
T_range = np.arange(0, 5, 0.04)
p_range = np.arange(0,1, 0.04)
X, Y = np.meshgrid(T_range, p_range)
#Z = np.vectorize(calcPi)(X, Y, 0)
Z = calcPi(T_range,p_range,0)

plt.figure(figsize=(8,8))
pi_plot = plt.contour(X, Y, Z, (0.1, 0.3, 0.5, 0.6, 0.7), colors='black')
pi_plotFill = plt.contourf(X, Y, Z, (0, 0.5),alpha=0.2)
plt.clabel(pi_plot, inline=True, fontsize= 10)
plt.xlabel("toxicity t")
plt.ylabel("fraction of mimics p")
plt.title("Contour plot of learnt behavior without taste-sampling")

X2, Y2 = np.meshgrid(T_range, p_range)
Z2 = calcPi(T_range, p_range, 1) #calculate pi for no sampling first

plt.figure(figsize=(8,8))
pi_plot_sampling = plt.contour(X2, Y2, Z2, (0.1, 0.3, 0.5, 0.6, 0.7), colors='black')
pi_plotFill = plt.contourf(X2, Y2, Z2, (0, 0.5),alpha=0.2)
plt.clabel(pi_plot_sampling, inline=True, fontsize= 10)
plt.xlabel("toxicity t")
plt.ylabel("fraction of mimics p")
plt.title("Contour plot of learnt behavior with taste-sampling");
# %%
