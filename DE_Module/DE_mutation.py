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



