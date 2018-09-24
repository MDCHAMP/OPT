import numpy as np
import random as rnd

def rand1 (pop, F, n):
    parent = pop.return_rnd(3, n)
    return parent[0].dna + F * (parent[1].dna-parent[2].dna) 
        
def rand2 (pop, F, n):
    parent = pop.return_rnd(5, n)
    return parent[0].dna + (F * (parent[1].dna - parent[2].dna)) + (F * (parent[3].dna - parent[4].dna)) 
    
def current2best (pop, F, n):
    parent  = pop.return_rnd(4 , n)
    current = pop.pool[n].dna
    best    = pop.best().dna
    return  current + (F * (best - current)) + (F * (parent[0].dna - parent[1].dna)) + (F * (parent[2].dna - parent[3].dna))
    
def current2rand (pop, F, n):
    parent  = pop.return_rnd(3 , n)
    current = pop.pool[n].dna
    return current + (F * (parent[0].dna - current)) + (F * (parent[1].dna - parent[2].dna))



class mutation_strategy:
    
    def __init__(self, gen_max):
        self.gen_max = gen_max
        self.strats  = [rand1, rand2, current2best, current2rand]  
        # muatation strategy functions
        self.sd      = np.array([[(0,0) for i in range(gen_max)] for j in range(4)])
        # self.sd[STRATEGY][GENERATION] = (SURVIVORS, DISCARDS)
        self.probs   = np.array([[0.25 for i in range(gen_max)] for j in range(4)]) 
        # self.probs[]
        self.current = np.zeros(gen_max)
        # Current stratgy index
    
    def update_mutation_strategy(self, LP, gen, srv, dis):
        probs = self.probs[:, gen]
        #print 'surviving', srv
        #print 'discarded', dis
        ########################################################################
        
        probs = ((srv + 1.0)**2 / (dis + srv + 1.0)) #+ rnd.uniform(0,0.01)

        ########################################################################
        target = sum(probs)
        probs = probs / target 
        #print 'new probs', probs
        count  = 0
        ind    = -1
        tgt = rnd.uniform(0,1)
        for prob in probs:
            count += prob
            ind += 1 
            if count >= tgt:
                self.current[gen+1] = ind
                #print 'new strat', self.strats[ind].__name__
                self.probs[:, gen+1] = probs
                return self.strats[ind]

        
    def strategy_plot(self, name, ymax):
        import matplotlib
        matplotlib.use('Agg')
        matplotlib.rcParams.update({'font.size': 12})
        import matplotlib.pyplot as plt
        from matplotlib.legend_handler import HandlerLine2D
        prob1 = np.zeros((self.gen_max))
        prob2 = np.zeros((self.gen_max))
        prob3 = np.zeros((self.gen_max))
        prob4 = np.zeros((self.gen_max))
        for i in range(self.gen_max):
            prob1[i] = self.probs[0][i]
            prob2[i] = self.probs[1][i]
            prob3[i] = self.probs[2][i]
            prob4[i] = self.probs[3][i]
        plt.figure()
        plt.plot(prob1, 'y-', label='Rand1/bin', hold=True)
        plt.plot(prob2, 'c-', label='Rand2/bin', hold=True)
        plt.plot(prob3, 'm-', label='Current2Best', hold=True)
        plt.plot(prob4, 'k-', label='Current2Rand', hold=True)
        plt.legend(loc=2)
        plt.xlabel('Generation')
        plt.ylabel('Relative Probabillity')
        #plt.axis([0, self.gen_max, 0, ymax])
        plt.savefig(name)
        
    

    
