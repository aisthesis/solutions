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

Using "coordinate descent", what is the error after 15 iterations?
Output:
initial error: 3.93039723188
1 u: -0.369542993197, v: -2.03992288047, dE/du: 13.695429932, dE/dv: 30.3992288047, E: 34.2901631123
2 u: 6.3924737648, v: -2.17869889007, dE/du: -67.6201675799, dE/dv: 1.38776009608, E: 0.534142591372
3 u: 6.37699523444, v: -2.28347262063, dE/du: 0.154785303603, dE/dv: 1.04773730554, E: 0.432660827324
4 u: 6.36460748637, v: -2.36821379387, dE/du: 0.123877480635, dE/dv: 0.847411732401, E: 0.365039735019
5 u: 6.35427658624, v: -2.43959481416, dE/du: 0.103309001286, dE/dv: 0.71381020293, E: 0.31646807536
6 u: 6.34542086477, v: -2.50137527574, dE/du: 0.0885572147852, dE/dv: 0.617804615793, E: 0.279763423064
7 u: 6.3376780617, v: -2.55589956861, dE/du: 0.0774280306526, dE/dv: 0.545242928711, E: 0.250986311675
8 u: 6.33080628124, v: -2.6047348478, dE/du: 0.0687178045794, dE/dv: 0.488352791906, E: 0.227783298944
9 u: 6.32463553422, v: -2.64898351269, dE/du: 0.0617074702093, dE/dv: 0.442486648913, E: 0.208656695724
10 u: 6.31904158643, v: -2.68945199663, dE/du: 0.0559394779331, dE/dv: 0.404684839323, E: 0.192605658614
11 u: 6.31393077346, v: -2.72674884919, dE/du: 0.0511081297136, dE/dv: 0.372968525671, E: 0.178934748408
12 u: 6.30923066644, v: -2.76134506639, dE/du: 0.0470010701459, dE/dv: 0.345962171983, E: 0.167145054343
13 u: 6.30488406577, v: -2.79361293379, dE/du: 0.0434660067154, dE/dv: 0.322678674029, E: 0.15686898733
14 u: 6.3008449881, v: -2.82385199281, dE/du: 0.0403907767263, dE/dv: 0.302390590196, E: 0.147829522524
15 u: 6.29707589931, v: -2.85230695408, dE/du: 0.0376908879242, dE/dv: 0.284549612635, E: 0.139813791996
(0.13981379199615315, 6.29707589930517, -2.852306954077811)
'''

import math

def minimize_error(u, v, eta):
    """ return iterations required, final u, final v """
    current_err = error(u, v)
    print "initial error: {0}".format(current_err)
    for i in range(1, 16):
        de_du = derr_du(u, v)
        u -= eta * de_du
        de_dv = derr_dv(u, v)
        v -= eta * de_dv
        current_err = error(u, v)
        print "{0} u: {1}, v: {2}, dE/du: {3}, dE/dv: {4}, E: {5}".format(i, 
                u, v, de_du, de_dv, current_err)
    return current_err, u, v

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
