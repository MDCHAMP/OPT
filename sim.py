




vector_field = []

y_vector = rk4.sim(vector_field)

def evaluate_fitness(y_vector, trial_transformation):
    
    np.dot(trial_transformation, y_vector)
    
    