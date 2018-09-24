import statistics as stat
from timeit import default_timer as timer
import DE as evo
import optimisation_functions as opt

suite_8D = [opt.Ackleys, opt.sphereN]
suite_2D = [opt.Ackleys, opt.Bukin6, opt.Dropwave, opt.Levy13, opt.sphereN, opt.easom]

a = [[-33, 33], [-33,33]]
b = [[-15, 5], [-3,3]]
c = [[-5.12,5.12], [-5.12,5.12]]
d = [[-10,10],[-10,10]]
e = [[-5.12,5.12], [-5.12,5.12]]
f = [[-100,100],[-100,100]]
g = [[-33,33]]*8
h = [[-5.12,5,12]]*8

bounds_2D = [a, b, c, d, e, f]
bounds_8D = [g, h]

N = 100
gen_max = 200
SADE_param = 0.5, 0.5
conv = None

RUNS = 25
def suite_2D():
    D = 2
    for i in range(6):
        av = []
        FES = []
        fit = suite_2D[i]
        bounds = bounds_2D[i]
        for run in range(RUNS):
            
            start_time = timer()
            SADE = evo.DE(N, D, gen_max, bounds, 
                                                                SADE_param, fit)
            SADE.run(conv)
            stop_time = timer()
            SADE.genome.convergence_plot('DE_out_conv_'+fit.__name__, 1)
            print 'Run number:', run
            #print 'Function', fit.__name__, ' in ', D, ' Dimensions' 
            #print 'time elapsed:', (stop_time - start_time) 
            #print 'Best gene:', SADE.genome.gen[SADE.gen].best().dna
            #print 'Best fit: ', SADE.genome.gen[SADE.gen].best().fitness
            #print 'Number of function evaluations:', SADE.nfe
            FES.append(SADE.FES_1k)
            av.append(SADE.genome.gen[SADE.gen].best().fitness)
        print 'Function', fit.__name__, ' in ', D, ' Dimensions has Best fitness of', min(av)    
        print 'Function', fit.__name__, ' in ', D, ' Dimensions has average fitness of', stat.mean(av) 
        print 'Function', fit.__name__, ' in ', D, ' Dimensions has STdev fitness of', stat.stdev(av) 
        print 'Function', fit.__name__, ' in ', D, ' Dimensions has 1k FES error of', stat.mean(FES)
        
D = 8
for i in range(2):
    av = []
    FES = []
    fit = suite_8D[i]
    bounds = bounds_8D[i]
    for run in range(RUNS):
        
        start_time = timer()
        SADE = evo.differential_evolution(N, D, gen_max, bounds, 
                                                            SADE_param, fit)
        SADE.run(conv)
        stop_time = timer()
        SADE.genome.convergence_plot('DE_out_conv8_'+fit.__name__, 1)
        print 'Run number:', run
        #print 'Function', fit.__name__, ' in ', D, ' Dimensions' 
        #print 'time elapsed:', (stop_time - start_time) 
        #print 'Best gene:', SADE.genome.gen[SADE.gen].best().dna
        #print 'Best fit: ', SADE.genome.gen[SADE.gen].best().fitness
        #print 'Number of function evaluations:', SADE.nfe
        FES.append(SADE.FES_1k)
        av.append(SADE.genome.gen[SADE.gen].best().fitness)
    print 'Function', fit.__name__, ' in ', D, ' Dimensions has Best fitness of', min(av)   
    print 'Function', fit.__name__, ' in ', D, ' Dimensions has average fitness of', stat.mean(av) 
    print 'Function', fit.__name__, ' in ', D, ' Dimensions has STdev fitness of', stat.stdev(av)
    print 'Function', fit.__name__, ' in ', D, ' Dimensions has 1k FES error of', stat.mean(FES)
        
        