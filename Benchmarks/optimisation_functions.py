import numpy as np
import random as rnd
import math

def Ackleys (vector):# Fitness function [Ackleys] ND problem GM@ x_i = 0 f(X) = 0
	d = np.size(vector) #accounting for F, CR, Fittness
	c = 2 * math.pi # a, b, c, are tuneable constants
	b = 0.2
	a = 20
	sum1 = 0
	sum2 = 0
	for i in range(d):
		xi = vector[i] # Evaluate on [-33, 33] for all xi
		sum1 = sum1 + (xi**2)
		sum2 = sum2 + math.cos(c * xi)

	term1 = - a * math.exp( -b * ((sum1 / d) **0.5))
	term2 = - math.exp(sum2 / d)
	y = term1 + term2 + a + math.exp(1)
	return y
# SADE is able to find the GM reliably with 7-9k function calls

def Ackley_score(best, nfe):
	gm    = [0,0]
	diff  = 1
	mse   = (gm-best)**2
	score = (mse * nfe / diff)
	

def Bukin6 (vector): # Fitness function [Buking no6] 2D problem GM@ [-10, 1] f(x) = 0
	x1 = vector[0] #evaluate on [-15, 5]
	x2 = vector[1] #evaluate on [-3, 3]
	term1 = 100 * (abs(x2 - 0.01 * x1**2))**0.5
	term2 = 0.01 * abs(x1 + 10)
	y = term1 + term2
	return y
# SADE allways finds a low cost solution but not always the GM

def Dropwave (vector):# Finess function  [Dropwave] 2D problem GM@ x* = [0, 0] f(x) = 0
	x1 = vector[0] # evaluate on [-5.12, 5.12] for all xi
	x2 = vector[1]
	frac1 = 1 + math.cos(12 * (((x1**2) + (x2**2))**0.5))
	frac2 = 0.5 * ((x1**2) + (x2**2)) + 2
	y = (-frac1 / frac2) + 1
	return y
# SADE finds the GM in <1k function calls

def Levy13 (vector):# Fitness function [Levy no13] 2D problem GM@ X* = [1, 1] f(x) = 0
	x1 = vector[0] # Evaluate on [-10, 10] for all xi
	x2 = vector[1]
	term1 = (math.sin(3 * math.pi * x1))**2
	term2 = (x1-1)**2 * (1+(math.sin(3 * math.pi * x2))**2)
	term3 = (x2-1)**2 * (1+(math.sin(2 * math.pi * x2))**2)
	y = term1 + term2 + term3
	return y
# SADE finds the GM very quickly

def sphereN (vector):# Fitness function [sphereN] ND problem GM@ x_i = 0 f(x)
	d = len(vector)
	sum = 0
	for i in range(d):
		xi = vector[i] #evaluate over [-5.12, 5.12] forall xi
		sum += xi**2
	y = sum
	return y
# SADE finds the GM extremely quickly <500 function evaluations

def sumsquares (vector):# Fitness function [sum squares] ND problem GM@ x_i = 0 f(x) = 0
	d = len(vector)
	sum = 0
	for i in range(d):
		xi = vector[i] #evaluate over [-10, 10] forall xi
		sum += (i+1) * (xi**2)
	y = sum
	return y

def easom (vector): #Fitness function [easom] 2D problem GM@ [pi, pi] f(x) = 0
	x1 = vector[0] #evauate over [-100, 100] for all xi
	x2 = vector[1]
	fact1 = -math.cos(x1) * math.cos(x2)
	fact2 = math.exp( -(x1 - math.pi)**2 -(x2 - math.pi)**2)
	y = (fact1 * fact2) + 1
	return y
# SADE finds the global minima very reliably

def griewank (vector): #Fitness function [griewank] ND problem GM@ xi = 0 f(x) = 0
	d = len(vector) - 3 #accounting for R, CR and fitness values
	sum = 0
	prod = 1
	for i in range(d):
		xi = vector[i] # Evaluate over [-600, 600] for all xi
		sum = sum + ((xi**2) / 4000)
		prod = prod * math.cos(xi / ((i + 1)**0.5))
	y = sum - prod + 1
	return y
# SADE always finds low cost solution; finds the GM fairly reliably for low dimensions but rarely finds it when D > 3



