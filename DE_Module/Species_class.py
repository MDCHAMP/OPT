################################################################################
#                    Automatic species builder - play god!
#
#       --Call the species class with the following variables
#
#   N       = Maximum population size
#   D       = Number of discrete genes in the DNA of an individual
#   gen_max = Number of generations to be allocated memory
#   hypers  = List of hyperparameters to be passed to every individual
#
#       --This allocates data for a species, to initiallise the first generation
#       use the species methods:
#
#   species.initialise(bounds)
#       Initialise the 0th generation of the species with random DNA
#       DNA is assigned by a uniform random distribution limits as per bounds
#
#   species.convergence_plot()
#       Plots the best and mean fitness convergence for the species against gen
#
#   species.meteor() 
#       Destroys the population with a meteor/ash cloud combo
#
#       --To interact directly with a specific generation use species.gen[n],
#       the generation level methods are:
#
#   species.gen[].rnd_sample(n, excl)
#       Returns n random individuals from the population
#
#   species.gen[].best_fit()
#       Returns the individual with the best fitness value
#                
#   species.gen[].mean_fit()
#       Returns the arithmetic mean of the fitnesses in a generation 
#
#   species.gen[].nuke(std)
#       Pertubates the current population dna with standard deviation std
#
#       --Operations at the individual level are called by referencing 
#       a specific individual:
#
#   species.gen[].pool[].dna
#       Returns the dna of a specific individual
#
#   species.gen[].pool[].fitness
#       Returns the fitness of the individual
#
#   species.gen[].pool[].kill()
#       'this kills the instance'
#        
################################################################################

import numpy as np
import random as rnd

class gene:
    def __init__(self, D, hypers, n):
        self.n = n
        self.dna = np.zeros((D))
        self.trial = np.zeros((D))
        self.hyper = hypers
        self.fitness= 10.0**300
    
    def apply_bounds (self, bounds):
        for i in range(len(self.dna)):
            if self.dna[i] < bounds[i][0]:
                #self.dna[i] += (bounds[i][0] - self.dna[i])*0.25
                self.dna[i] = bounds[i][0]
                #print 'too small'
            elif self.dna[i] > bounds[i][1]:
                #self.dna[i] += (bounds[i][1] - self.dna[i])*0.25
                self.dna[i] = bounds[i][1]
                #print 'too big'

        
        
class gene_pool:
    def __init__(self, N, D, hypers):
        self.pool = np.zeros((N), dtype=object)
        for i in range(N):
            self.pool[i] = gene(D, hypers, i)
        self.survivors = 0
        self.discards = 0
        self.F = 0.0
        self.CR = 0.0

    def return_rnd(self, n, excl=None):
        size = range(len(self.pool))
        if excl != None:
            size.remove(excl)
        key = rnd.sample(size, n)
        sample = np.zeros((n), dtype=object)
        for i in range(n):
            sample[i] = self.pool[key[i]]
        return sample
            
    def best(self):
        top  = 10**300
        best = 0
        for gene in self.pool:
            if gene.fitness < top:
                best = gene
                top  = gene.fitness
        return best

        
    def best_fit(self):
        top = 10.1**300
        for gene in self.pool:
            if gene.fitness < top:
                top = gene.fitness
        return top    
   
    def mean_fit(self):
        add = 0.0
        ind = 0.0
        for gene in self.pool:
            add += gene.fitness
            ind += 1
        return add / ind    
        
class species:
    def __init__(self, N, D, gen_max, hypers=None):
        self.gen = np.zeros((gen_max), dtype=object)
        self.gen_max = gen_max
        self.D = D
        self.N = N
        for i in range(gen_max):
            self.gen[i] = gene_pool(N, D, hypers)
            
    def initialise(self, boundry_vector):
        for gene in self.gen[0].pool:
            for i in range(self.D):
                gene.dna[i] = rnd.uniform(boundry_vector[i][0], boundry_vector[i][1])
    
    def initial_fit(self, fit):   
        for gene in self.gen[0].pool:
            gene.fitness = fit(gene.dna)
            
    def convergence_plot(self, name, fitmax):
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        
        aver = np.zeros((self.gen_max))
        mean = np.zeros((self.gen_max))
        for i in range(self.gen_max):
            aver[i] = self.gen[i].best().fitness
            mean[i] = self.gen[i].mean_fit()
       
        plt.figure()
        plt.plot(aver, 'r-', label='Best', hold=True)
        plt.plot(mean, 'b--', label='Mean', hold=True)
        plt.xlabel('Generation')
        plt.ylabel('Fitness')
        plt.legend()
        plt.axis([0, self.gen_max, 0, fitmax])
        plt.savefig(name)    


