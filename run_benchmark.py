from Benchmarks import suites
from DE_Module import DE as evo

#Hyper_parmaeters
F =  0.5 
Cr = 0.2


N = 50
D = None
gen_max = 200

hypers = [F, Cr]
pop_param = [N, D, gen_max]

Test1 = suites.suite_2D(evo.DE, hypers, pop_param)
Test1.run(10)

#Test2 = suites.suite_8D(evo.DE, Hypers, pop_param)
#Test2.run(10)