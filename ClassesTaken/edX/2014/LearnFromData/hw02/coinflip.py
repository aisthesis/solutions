'''
Copyright (c) 2014 Marshall Farrier
license http://opensource.org/licenses/gpl-license.php GNU Public License

@author: Marshall Farrier
@contact: marshalldfarrier@gmail.com
@since: 2014-10-12
@summary: Homework 2: coinflips
'''

import random
import sys

def flip(p_heads=0.5, n_flips=10):
    n_heads = 0
    for i in range(n_flips):
        n_heads += 1 if random.random() <= p_heads else 0
    return n_heads

def flips(n_trials=1000, p_heads=0.5, n_flips=10):
    results = [0] * n_trials
    for i in range(n_trials):
        results[i] = flip(p_heads, n_flips)
    nu1 = results[0] / 10.0
    nu_rand = results[random.randrange(n_trials)] / 10.0
    nu_min = min(results) / 10.0
    return nu1, nu_rand, nu_min

def repeat_flips(n_repetitions=100000, n_trials=1000, p_heads=0.5, n_flips=10):
    nu1_sum = nu_rand_sum = nu_min_sum = 0.0
    nu1 = nu_rand = nu_min = 0.0
    for i in range(n_repetitions):
        if (i + 1) % 10000 == 0:
            print("\nRepetition {0}".format(i + 1)),
            sys.stdout.flush()
        elif i > 10000 and i % 1000 == 0:
            print('.'),
            sys.stdout.flush()
        nu1, nu_rand, nu_min = flips(n_trials, p_heads, n_flips)
        nu1_sum += nu1
        nu_rand_sum += nu_rand
        nu_min_sum += nu_min
    return nu1_sum / n_repetitions, nu_rand_sum / n_repetitions, nu_min_sum / n_repetitions 
