import statistics as stat
from timeit import default_timer as timer
import optimisation_functions as opt

class suite_2D:
    
    def __init__(self, optimiser, optimiser_hypers, pop_param):
        
        a = [[-33, 33], [-33,33]]
        b = [[-15, 5], [-3,3]]
        c = [[-5.12,5.12], [-5.12,5.12]]
        d = [[-10,10],[-10,10]]
        e = [[-5.12,5.12], [-5.12,5.12]]
        f = [[-100,100],[-100,100]]
        
        self.suite_2D = [opt.Ackleys, opt.Bukin6, opt.Dropwave, opt.Levy13, opt.sphereN, opt.easom]
        self.bounds_2D = [a, b, c, d, e, f]
        
        self.evo = optimiser
        
        self.hypers = optimiser_hypers
        
        N, D, gen = pop_param
        self.pop_param = [N, 2, gen]
        
        
    def run(self, n_runs):   
        with open('Benchmarks/2D_outputs/2D_Results.text', 'w') as f:
            for function, limit in zip(self.suite_2D, self.bounds_2D):
                f.write('Function: '+function.__name__+'\n')
                f.write("{: <5} {: <15} {: <15} {: <15}\n".format('Run', 'Best', 'Mean', 'std'))
                b = []
                m = []
                v = []
                for run in range(n_runs):
                    actual = self.evo(self.hypers, self.pop_param, limit, function)
                    actual.run()
                    
                    best = actual.genome.gen[actual.gen].best_fit()
                    best_vect = actual.genome.gen[actual.gen].best().dna
                    mean = actual.genome.gen[actual.gen].mean_fit()
                    std = actual.genome.gen[actual.gen].std_fit()
                    
                    b.append(best)
                    v.append(best_vect)
                    m.append(mean)
                    
                    f.write("{: <5} {: <15,.10f} {: <15,.10f} {: <15,.10f}\n".format(run+1,best,mean,std))
                    
                f.write('Overall best fitness: '+str(min(b))+'\n')
                f.write('Achieved by parameters: '+str(v[b.index(min(b))])+'\n')
                f.write('True global minima is at: '+'[0.,0.]'+'\n\n\n')
                
                actual.genome.convergence_plot('Benchmarks/2D_outputs/2D_benchmark_convergence_plot_for_'+function.__name__+'.png', 20)

