from Benchmarks import suites 
from DE_Module import DE as evo1
from SADE_Module import SADE as evo2


#Hyper_parmaeters
Fm =  0.9 
Crm = 0.5
lp = 20
#Pop_param
N = 100
D = 2
gen_max = 1000

hypers = [Fm, Crm, lp]
pop_param = [N, 2, gen_max]

#Test1 = suites.suite_2D(evo2.SADE, hypers, pop_param)
#Test1.run(10)

hypers = [Fm, Crm, lp]
pop_param = [N, 8, gen_max]
Test2 = suites.suite_ND(evo2.SADE, hypers, pop_param)
Test2.run(1)