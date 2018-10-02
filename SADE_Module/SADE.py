import numpy as np
import random as rnd
from Species_Module import Species_class as genome
import SADE_mutation as mu


class SADE:
    
    def __init__(self, hypers, pop_param, bounds, fitness):
        #Initialise hyperparameters and fitness function information
        self.Fm, self.Crm, self.learning_period = hypers
        self.N, self.D, self.Gen_max = pop_param
        self.bounds = bounds
        self.fitness = fitness
        #Initialise population and apply initial fitness values
        self.genome = genome.species(self.N, self.D, self.Gen_max)
        self.genome.initialise(self.bounds)
        self.genome.initial_fit(self.fitness)
        self.gen = 0
        #Initialise mutation strategies and 
        self.mutation_strategies = [mu.rand1(self.Gen_max), mu.rand2(self.Gen_max), mu.current2best(self.Gen_max), mu.current2rand(self.Gen_max)]
        self.strategy_index = rnd.randint(0, 4)
        self.probability_history = np.array([[0.25 for i in range(self.Gen_max)] for j in range(len(self.mutation_strategies))]) 
        

        
    
    def update_SADE(self):
        probs = []
        learn_key = [(self.gen-self.learning_period), self.gen]
        for strat in self.mutation_strategies:
            s = strat.survivors[learn_key].sum()
            f = strat.failures[learn_key].sum()
            probs.append(       ((s + 1.0)**2 / (f + s + 1.0))  + s)#Strategy probability update model
            
        probs = probs / sum(probs)
        for i, prob in enumerate(probs):
            self.mutation_strategies[i].probability = prob
        
        self.Crm = 0.5
        self.Fm = 0.3 
       
            
    
    def select_mutation_strategy(self):
        pick  = rnd.uniform(0,1)
        place = 0.0
        for i, strategy in enumerate(self.mutation_strategies):
            self.probability_history[i][self.gen] = strategy.probability
        for i, strategy in enumerate(self.mutation_strategies):
            place += strategy.probability
            if place > pick:
                self.strategy_index = i
                return strategy.mutate
                
                
    def select_hyperparameters(self):
        F  = rnd.gauss(self.Fm,0.3)
        Cr = rnd.gauss(self.Crm,0.1)
        return F, Cr

        
        
    def generation(self):
        if (self.gen % self.learning_period) == 0 and self.gen > self.learning_period:
            self.update_SADE()
        
        pop = self.genome.gen[self.gen]
        for gene in pop.pool:
            f, cr = self.select_hyperparameters()
            #Apply mutation and ensure vectors remain within given bounds
            gene.trial = self.select_mutation_strategy()(pop, f, gene.n)
            gene.apply_bounds(self.bounds)
            #Apply crossover and ensure that some changes are made to the trial vector
            crossover_key = np.random.rand(self.D) > cr
            if np.any(crossover_key):
                crossover_key[0] = False
            gene.trial = np.where(crossover_key, gene.dna, gene.trial)
            #Evaluate new fitness and update next generation       
            new_fitness = self.fitness(gene.trial)
            if new_fitness < gene.fitness:
                self.genome.gen[self.gen+1].pool[gene.n].dna     = gene.trial
                self.genome.gen[self.gen+1].pool[gene.n].fitness = new_fitness
                self.mutation_strategies[self.strategy_index].survivors[self.gen] += 1
            else:
                self.genome.gen[self.gen+1].pool[gene.n] = gene
                self.mutation_strategies[self.strategy_index].failures[self.gen] += 1
   
                
    def run(self):
        while self.gen < self.Gen_max-1:
            self.generation()
            self.gen += 1 
        
        mu.plot_strategy_probabilities(self.mutation_strategies, self.probability_history, 'SADE_Module/Strategy_plot.png')