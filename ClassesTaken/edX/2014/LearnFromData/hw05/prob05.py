'''
Copyright (c) 2014 Marshall Farrier
license http://opensource.org/licenses/gpl-license.php GNU Public License

@author: Marshall Farrier
@contact: marshalldfarrier@gmail.com
@since: 2014-11-01
@summary: Gradient descent exercise

Error is given by E(u,v) = (u * e^v - 2 * v * e^(-u))^2
dE/du = 2 * (u * exp(v) - 2 * v * exp(-u)) * (exp(v) + 2 * v * exp(-u))
dE/dv = 2 * (u * exp(v) - 2 * v * exp(-u)) * (u * exp(v) - 2 * exp(-u))

eta is 0.1 (learning rate)
starting point is (1, 1)

How many iterations are required for E(u,v) to fall below 10^(-14)?
Output:
initial error: 3.93039723188
1 u: -0.369542993197, v: 0.213920553625, dE/du: 13.695429932, dE/dv: 7.86079446375, E: 1.15950972997
2 u: 0.0305206903513, v: -0.507934045444, dE/du: -4.00063683548, dE/dv: 7.21854599068, E: 1.00740748296
3 u: 0.107523114199, v: -0.122210255574, dE/du: -0.770024238477, dE/dv: -3.8572378987, E: 0.0990091216273
4 u: 0.0656448258149, v: -0.0151665598769, dE/du: 0.418782883841, dE/dv: -1.07043695697, E: 0.00866064536281
5 u: 0.0478411706217, v: 0.0184898992267, dE/du: 0.178036551932, dE/dv: -0.336564591037, E: 0.000181755791728
6 u: 0.0449994630994, v: 0.0234992516968, dE/du: 0.0284170752229, dE/dv: -0.0500935247005, E: 1.29723984784e-06
7 u: 0.0447560190293, v: 0.0239242964704, dE/du: 0.00243444070088, dE/dv: -0.00425044773605, E: 7.29152469846e-09
8 u: 0.0447377460407, v: 0.0239561747966, dE/du: 0.000182729886684, dE/dv: -0.00031878326216, E: 4.00999789056e-11
9 u: 0.0447363908175, v: 0.0239585389222, dE/du: 1.35522316999e-05, dE/dv: -2.36412563482e-05, E: 2.20168344841e-13
10 u: 0.0447362903978, v: 0.0239587140991, dE/du: 1.00419725016e-06, dE/dv: -1.75176893143e-06, E: 1.20868339442e-15
(10, 0.04473629039778207, 0.023958714099141746)
'''

import math

def minimize_error(u, v, eta):
    """ return iterations required, final u, final v """
    current_err = error(u, v)
    i = 0
    print "initial error: {0}".format(current_err)
    while current_err > 10**(-14):
        i += 1
        de_du = derr_du(u, v)
        de_dv = derr_dv(u, v)
        u -= eta * de_du
        v -= eta * de_dv
        current_err = error(u, v)
        print "{0} u: {1}, v: {2}, dE/du: {3}, dE/dv: {4}, E: {5}".format(i, 
                u, v, de_du, de_dv, current_err)
    return i, u, v

def error(u, v):
    return (u * math.exp(v) - 2.0 * v * math.exp(-u))**2

def derr_du(u, v):
    exp_v = math.exp(v)
    exp_minus_u = math.exp(-u)
    return 2.0 * (u * exp_v - 2.0 * v * exp_minus_u) * (exp_v + 2.0 * v * exp_minus_u)

def derr_dv(u, v):
    exp_v = math.exp(v)
    exp_minus_u = math.exp(-u)
    return 2.0 * (u * exp_v - 2.0 * v * exp_minus_u) * (u * exp_v - 2.0 * exp_minus_u)

if __name__ == '__main__':
    print minimize_error(1.0, 1.0, 0.1)
