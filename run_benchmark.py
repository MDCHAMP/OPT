from Benchmarks import suites 
from DE_Module import DE as evo


#To Run: python -m Benchmarks.run_benchmark.py
#

#Hyper_parmaeters
F =  0.5 
Cr = 0.2
#Pop_param
N = 50
D = 2
gen_max = 100

hypers = [F, Cr]
pop_param = [N, 2, gen_max]

Test1 = suites.suite_2D(evo.DE, hypers, pop_param)
Test1.run(10)

hypers = [F, Cr]
pop_param = [N, 8, gen_max]
Test2 = suites.suite_ND(evo.DE, hypers, pop_param)
Test2.run(10) 