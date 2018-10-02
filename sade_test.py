from Benchmarks import optimisation_classes as opt
from SADE_Module import SADE as evo

#Hyper_parmaeters
F =  0.5 
Cr = 0.2
lp = 10
hypers = [F, Cr, lp]

#Pop_param
N = 50
D = 2
gen_max = 100
pop_param = [N, 2, gen_max]

#Bounds, fitnes_function
function = opt.ackleys(D)
bounds = function.bounds
fitness = function.fit


test = evo.SADE(hypers, pop_param, bounds, fitness)
test.run()

