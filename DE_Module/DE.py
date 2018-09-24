import numpy as np
import random as rnd
import Species_class as genome
import mutation as mu


class DE:
    
    def __init__(self, hypers, pop_param, bounds, fitness):
        
        self.F, self.Cr = hypers
        
        self.N, self.D, self.Gen_max = pop_param
        
        self.bounds = bounds
        
        self.fitness = fitness
        
        self.genome = genome.species(self.N, self.D, self.Gen_max)
        self.genome.initialise(self.bounds)
        self.genome.initial_fit(self.fitness)
        self.gen = 0
        

        
    def generation(self):

        pop = self.genome.gen[self.gen]
        donor = pop.return_rnd(1)[0].dna
        Irand = rnd.randint(0, self.D)
        
        for gene in pop.pool:
            
            gene.trial = mu.rand1(pop, self.F, gene.n)
            gene.apply_bounds(self.bounds)
            
            for i, donor_dna in enumerate(donor):

                if rnd.uniform(0, 1) < self.Cr or i == Irand:
                   gene.trial[i] = donor_dna
                   
            new_fitness = self.fitness(gene.trial)
        
            if new_fitness < gene.fitness:
                self.genome.gen[self.gen+1].pool[gene.n].dna     = gene.trial
                self.genome.gen[self.gen+1].pool[gene.n].fitness = new_fitness
            else:
                self.genome.gen[self.gen+1].pool[gene.n] = gene
                
    def run(self):

        while self.gen < self.Gen_max-1:

            self.generation()
            self.gen += 1 