import statistics as stat
from timeit import default_timer as timer
import optimisation_classes as opt

class suite_2D:
    
    def __init__(self, optimiser, optimiser_hypers, pop_param):
        

        self.suite_2D = [opt.ackleys(2), opt.sphereN(2), opt.sumsquares(2), opt.griewank(2), opt.bukin6(), opt.dropwave(), opt.levy13(), opt.easom()]

        N, D, gen = pop_param
        self.pop_param = [N, 2, gen]
        self.evo = optimiser
        self.hypers = optimiser_hypers
        
    def run(self, n_runs):   
        with open('Benchmarks/2D_outputs/2D_Results.text', 'w+') as f:
            f.write('2D benchmark suite evaluating the performance of '+self.evo.__name__+' \non a suite of benchmark optimisation functions from  the vitrual library of simulation experiments.\n\n\n')
            for function in self.suite_2D:
                f.write('Function: '+function.__class__.__name__+'\n')
                f.write("{: <5} {: <15} {: <15} {: <15}\n".format('Run', 'Best', 'Mean', 'std'))
                b = []
                m = []
                v = []
                overall_best_run = 100**300 
                for run in range(n_runs):
                    actual = self.evo(self.hypers, self.pop_param, function.bounds, function.fit)
                    actual.run()
                    
                    best = actual.genome.gen[actual.gen].best_fit()
                    best_vect = actual.genome.gen[actual.gen].best().dna
                    mean = actual.genome.gen[actual.gen].mean_fit()
                    std = actual.genome.gen[actual.gen].std_fit()
                    
                    b.append(best)
                    v.append(best_vect)
                    m.append(mean)
                    
                    f.write("{: <5} {: <15,.10f} {: <15,.10f} {: <15,.10f}\n".format(run+1,best,mean,std))
                    
                    if best < overall_best_run:
                        best_genome = actual.genome
                    
                f.write('Overall best fitness: '+str(min(b))+'\n')
                f.write('Achieved by parameters: '+str(v[b.index(min(b))])+'\n')
                f.write('True global minima is at: '+str(function.gm)+'\n')
                f.write('True best parameters are: '+str(function.truth)+'\n\n\n')
                
                best_genome.convergence_plot('Benchmarks/2D_outputs/Best_2D_benchmark_convergence_plot_for_'+function.__class__.__name__+'.png', function.roof)
                best_genome.export_genome('Benchmarks/2D_outputs/Best_genome_for_'+function.__class__.__name__)

class suite_ND:
    
    def __init__(self, optimiser, optimiser_hypers, pop_param):

        N, D, gen = pop_param
        self.D = D
        self.suite_ND = [opt.ackleys(D), opt.sphereN(D), opt.sumsquares(D), opt.griewank(D)]
        self.pop_param = [N, D, gen]
        self.evo = optimiser
        self.hypers = optimiser_hypers
        
    def run(self, n_runs):   
        with open('Benchmarks/'+str(self.D)+'D_outputs/'+str(self.D)+'D_Results.text', 'w+') as f:
            f.write(''+str(self.D)+'D benchmark suite evaluating the performance of '+self.evo.__name__+' \non a suite of benchmark optimisation functions from  the vitrual library of simulation experiments.\n\n\n')
            for function in self.suite_ND:
                f.write('Function: '+function.__class__.__name__+'\n')
                f.write("{: <5} {: <15} {: <15} {: <15}\n".format('Run', 'Best', 'Mean', 'std'))
                b = []
                m = []
                v = []
                overall_best_run = 100**300 
                for run in range(n_runs):
                    actual = self.evo(self.hypers, self.pop_param, function.bounds, function.fit)
                    actual.run()
                    
                    best = actual.genome.gen[actual.gen].best_fit()
                    best_vect = actual.genome.gen[actual.gen].best().dna
                    mean = actual.genome.gen[actual.gen].mean_fit()
                    std = actual.genome.gen[actual.gen].std_fit()
                    
                    b.append(best)
                    v.append(best_vect)
                    m.append(mean)
                    
                    f.write("{: <5} {: <15,.10f} {: <15,.10f} {: <15,.10f}\n".format(run+1,best,mean,std))
                    
                    if best < overall_best_run:
                        best_genome = actual.genome
                    
                f.write('Overall best fitness: '+str(min(b))+'\n')
                f.write('Achieved by parameters: '+str(v[b.index(min(b))])+'\n')
                f.write('True global minima is at: '+str(function.gm)+'\n')
                f.write('True best parameters are: '+str(function.truth)+'\n\n\n')
                
                best_genome.convergence_plot('Benchmarks/'+str(self.D)+'D_outputs/Best_'+str(self.D)+'D_benchmark_convergence_plot_for_'+function.__class__.__name__+'.png', function.roof)
                best_genome.export_genome('Benchmarks/'+str(self.D)+'D_outputs/Best_genome_for_'+function.__class__.__name__)