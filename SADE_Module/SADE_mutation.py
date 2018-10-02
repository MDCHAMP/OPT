import numpy as np
import random as rnd

class rand1:
    def __init__(self, generations):
        self.probability = 0.25
        self.survivors = np.zeros((generations))
        self.failures    = np.zeros((generations))
    
    def mutate (self, pop, F, n):
        parent = pop.return_rnd(3)
        return parent[0].dna + F * (parent[1].dna-parent[2].dna) 
        
        
        
class rand2:
    def __init__(self, generations):
        self.probability = 0.25
        self.survivors = np.zeros((generations))
        self.failures    = np.zeros((generations))
    
    def mutate (self, pop, F, n):
        parent = pop.return_rnd(5)
        return parent[0].dna + (F * (parent[1].dna - parent[2].dna)) + (F * (parent[3].dna - parent[4].dna)) 
                
        
        
class current2best:
    def __init__(self, generations):
        self.probability = 0.25
        self.survivors = np.zeros((generations))
        self.failures    = np.zeros((generations))

    def mutate (self, pop, F, n):
        parent  = pop.return_rnd(4)
        current = pop.pool[n].dna
        best    = pop.best().dna
        return  current + (F * (best - current)) + (F * (parent[0].dna - parent[1].dna)) + (F * (parent[2].dna - parent[3].dna))
  
  
    
class current2rand:
    def __init__(self, generations):
        self.probability = 0.25
        self.survivors = np.zeros((generations))
        self.failures    = np.zeros((generations))
    
    def mutate (self, pop, F, n):
        parent  = pop.return_rnd(3)
        current = pop.pool[n].dna
        return current + (F * (parent[0].dna - current)) + (F * (parent[1].dna - parent[2].dna))
        
    
    

def plot_strategy_probabilities(probs, history, name):
    import matplotlib
    matplotlib.use('Agg')
    matplotlib.rcParams.update({'font.size': 12})
    import matplotlib.pyplot as plt
    from matplotlib.legend_handler import HandlerLine2D
    
    plt.figure()
    for i, strat in enumerate(probs):
        plt.plot(history[i][:], label=strat.__class__.__name__, hold=True)
    plt.legend(loc=2)
    plt.xlabel('Generation')
    plt.ylabel('Relative Probabillity')
    plt.savefig(name)
        
        
        
    
  
    
