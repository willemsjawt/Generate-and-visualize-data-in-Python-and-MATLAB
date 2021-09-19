# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

"""### Mean, median, standard deviation, variance"""

## mean (aka average or arithmetic mean)

# some numbers
vect = [ 1,2,3,2 ]
n = len(vect)

# mean by definition
meanval1 = sum(vect) / n

# mean by function
meanval2 = np.mean(vect)

print(meanval1,meanval2)

## median

## easiest to the use the built-in function
medianval = np.median(vect)

print(medianval)

## standard deviation

# first, mean-center
vectC = vect - np.mean(vect)

# then, sum of squared elements, divide by N-1, take square root
stdval1 = np.sqrt( np.sum( vectC**2) / (n-1))

# or use the function
stdval2 = np.std(vect,ddof=1) # note the second input to provide an unbiased estimate

print(stdval1,stdval2)

## variance

# it's standard deviation squared
varval1 = stdval1**2

# or use the function
varval2 = np.var(vect,ddof=1)

print(varval1,varval2)

