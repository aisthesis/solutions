"""
Copyright (c) 2014 Marshall Farrier
license http://opensource.org/licenses/MIT

@author: Marshall Farrier
@contact: marshalldfarrier@gmail.com
@since: 2014-11-20
@summary: Problems 2-?
https://courses.edx.org/c4x/CaltechX/CS_1156x/asset/hw8fsew3e.pdf
"""

from svmutil import *
import numpy as np

def get(fname):
    """ return x, y """
    raw_data = np.loadtxt("data/{0}".format(fname))
    y = np.empty((raw_data.shape[0]), dtype=int)
    np.around(raw_data[:, 0], out=y)
    return raw_data[:, 1:], y

def get_err(features, labels, model):
    acc = svm_predict(labels, features, model)[1]
    return 1.0 - acc[0] / 100.0

def one_vs_all(x, y, digit):
    """
    returns new features and labels where the given
    digit has label 1 and all other digits have label -1
    """
    labels = np.ones(y.shape)
    labels[y != digit] = -1
    return x.tolist(), labels.tolist()

def one_vs_one(x, y, digit1, digit2):
    """
    returns new features and labels where any
    row not corresponding to digit1 or digit2 is removed
    and where digit1 gets label 1, digit2 label -1
    """
    mask = ((y == digit1) + (y == digit2))
    features = x[mask, :]
    labels = y[mask]
    labels[labels == digit2] = -1
    labels[labels == digit1] = 1
    return features.tolist(), labels.tolist()

def prob2():
    """ Output: (0, 0.10588396653408305) """
    param = svm_parameter('-c 0.01 -t 1 -d 2 -g 1 -r 1 -h 0')
    x, y = get('features.train')
    highesterr = 0.0
    worstdigit = -1
    for i in range(0, 10, 2):
        features, labels = one_vs_all(x, y, i)
        prob = svm_problem(labels, features)
        m = svm_train(prob, param)
        err = get_err(features, labels, m)
        print "error for digit {0}: {1}".format(i, err)
        if err > highesterr:
            highesterr = err
            worstdigit = i
    return worstdigit, highesterr

def prob3():
    """ Output: (1, 0.014401316691811883) """
    param = svm_parameter('-c 0.01 -t 1 -d 2 -g 1 -r 1 -h 0')
    x, y = get('features.train')
    lowesterr = 1.0
    bestdigit = -1
    for i in range(1, 10, 2):
        features, labels = one_vs_all(x, y, i)
        prob = svm_problem(labels, features)
        m = svm_train(prob, param)
        err = get_err(features, labels, m)
        print "error for digit {0}: {1}".format(i, err)
        if err < lowesterr:
            lowesterr = err
            bestdigit = i
    return bestdigit, lowesterr

def prob4():
    """ Output: 1794 """
    param = svm_parameter('-c 0.01 -t 1 -d 2 -g 1 -r 1 -h 0')
    x, y = get('features.train')
    features, labels0 = one_vs_all(x, y, 0)
    _, labels1 = one_vs_all(x, y, 1)
    prob1 = svm_problem(labels1, features)
    prob0 = svm_problem(labels0, features)
    m0 = svm_train(prob0, param)
    m1 = svm_train(prob1, param)
    return abs(m1.get_nr_sv() - m0.get_nr_sv())

def ghost5ab(digit1=4, digit2=6):
    """ Output: [(0.001, 1160), (0.01, 1152), (0.1, 1133), (1, 1118)] """
    x, y = get('features.train')
    features, labels = one_vs_one(x, y, digit1, digit2)
    prob = svm_problem(labels, features)
    c_vs_nsvs = []
    for i in range(-3, 1):
        cost = 10**i
        param = svm_parameter("-c {0} -t 1 -d 2 -g 1 -r 1 -h 0".format(cost))
        m = svm_train(prob, param)
        c_vs_nsvs.append((cost, m.get_nr_sv()))
        print "C: {0}, support vectors: {1}".format(cost, m.get_nr_sv())
    return c_vs_nsvs

def prob5ab():
    """ Output: [(0.001, 76), (0.01, 34), (0.1, 24), (1, 24)] """
    return ghost5ab(1, 5)

def ghost5c(digit1=4, digit2=6):
    """
    Output:
    C vs. ein:
    [(0.001, 0.42173252279635254), (0.01, 0.4164133738601824), (0.1, 0.3905775075987842), (1, 0.3913373860182371)]
    C vs. eout:
    [(0.001, 0.427027027027027), (0.01, 0.42162162162162165), (0.1, 0.42162162162162165), (1, 0.42162162162162165)]
    """
    xtrain, ytrain = get('features.train')
    xtest, ytest = get('features.test')
    feat_train, lab_train= one_vs_one(xtrain, ytrain, digit1, digit2)
    feat_test, lab_test= one_vs_one(xtest, ytest, digit1, digit2)
    prob = svm_problem(lab_train, feat_train)
    c_vs_eout = []
    c_vs_ein = []
    for i in range(-3, 1):
        cost = 10**i
        param = svm_parameter("-c {0} -t 1 -d 2 -g 1 -r 1 -h 0".format(cost))
        m = svm_train(prob, param)
        ein = get_err(feat_train, lab_train, m)
        eout = get_err(feat_test, lab_test, m)
        c_vs_ein.append((cost, ein))
        c_vs_eout.append((cost, eout))
        print "C: {0}, eout: {1}".format(cost, eout)
    print "C vs. ein:"
    print c_vs_ein
    print "C vs. eout:"
    print c_vs_eout
    return c_vs_eout

def prob5c():
    """
    Output:
    [(0.001, 0.01650943396226412), (0.01, 0.018867924528301883), (0.1, 0.018867924528301883), (1, 0.018867924528301883)]
    """
    return ghost5c(1, 5)

def prob5d():
    """ Output: (0.0032030749519539325, 1) """
    digit1 = 1
    digit2 = 5
    xtrain, ytrain = get('features.train')
    feat_train, lab_train = one_vs_one(xtrain, ytrain, digit1, digit2)
    prob = svm_problem(lab_train, feat_train)
    bestein = 1.0
    bestc = -1
    for i in range(-3, 1):
        cost = 10**i
        param = svm_parameter("-c {0} -t 1 -d 2 -g 1 -r 1 -h 0".format(cost))
        m = svm_train(prob, param)
        ein = get_err(feat_train, lab_train, m)
        print "C: {0}, ein: {1}".format(cost, ein)
        if ein < bestein:
            bestein = ein
            bestc = cost
    return bestein, bestc

def ghost6a(digit1=4, digit2=6):
    """ Output: {'ein2': 0.43313069908814594, 'ein5': 0.39969604863221886} """
    xtrain, ytrain = get('features.train')
    cost = 0.0001
    feat_train, lab_train = one_vs_one(xtrain, ytrain, digit1, digit2)
    prob = svm_problem(lab_train, feat_train)
    param2 = svm_parameter("-c {0} -t 1 -d {1} -g 1 -r 1 -h 0".format(cost, 2))
    param5 = svm_parameter("-c {0} -t 1 -d {1} -g 1 -r 1 -h 0".format(cost, 5))
    m2 = svm_train(prob, param2)
    m5 = svm_train(prob, param5)
    ein2 = get_err(feat_train, lab_train, m2)
    ein5 = get_err(feat_train, lab_train, m5)
    return {'ein2': ein2, 'ein5': ein5}

def prob6a():
    """ {'ein2': 0.008968609865470878, 'ein5': 0.004484304932735439} """
    return ghost6a(1, 5)

def ghost6b(digit1=4, digit2=6):
    """ Output: {'sv5': 1111, 'sv2': 1160} """
    xtrain, ytrain = get('features.train')
    cost = 0.001
    feat_train, lab_train = one_vs_one(xtrain, ytrain, digit1, digit2)
    prob = svm_problem(lab_train, feat_train)
    param2 = svm_parameter("-c {0} -t 1 -d {1} -g 1 -r 1 -h 0".format(cost, 2))
    param5 = svm_parameter("-c {0} -t 1 -d {1} -g 1 -r 1 -h 0".format(cost, 5))
    m2 = svm_train(prob, param2)
    m5 = svm_train(prob, param5)
    return {'sv2': m2.get_nr_sv(), 'sv5': m5.get_nr_sv()}

def prob6b():
    """ Output: {'sv5': 25, 'sv2': 76} """
    return ghost6b(1, 5)

def ghost6c(digit1=4, digit2=6):
    """ Output: {'ein2': 0.4164133738601824, 'ein5': 0.39969604863221886} """
    xtrain, ytrain = get('features.train')
    cost = 0.01
    feat_train, lab_train = one_vs_one(xtrain, ytrain, digit1, digit2)
    prob = svm_problem(lab_train, feat_train)
    param2 = svm_parameter("-c {0} -t 1 -d {1} -g 1 -r 1 -h 0".format(cost, 2))
    param5 = svm_parameter("-c {0} -t 1 -d {1} -g 1 -r 1 -h 0".format(cost, 5))
    m2 = svm_train(prob, param2)
    m5 = svm_train(prob, param5)
    ein2 = get_err(feat_train, lab_train, m2)
    ein5 = get_err(feat_train, lab_train, m5)
    return {'ein2': ein2, 'ein5': ein5}

def prob6c():
    """ Output: {'ein2': 0.004484304932735439, 'ein5': 0.0038436899423446302} """
    return ghost6c(1, 5)

def ghost6d(digit1=4, digit2=6):
    """ Output: {'eout5': 0.3918918918918919, 'eout2': 0.42162162162162165} """
    xtrain, ytrain = get('features.train')
    xtst, ytst = get('features.test')
    cost = 1.0
    feat_train, lab_train = one_vs_one(xtrain, ytrain, digit1, digit2)
    feat_tst, lab_tst = one_vs_one(xtst, ytst, digit1, digit2)
    prob = svm_problem(lab_train, feat_train)
    param2 = svm_parameter("-c {0} -t 1 -d {1} -g 1 -r 1 -h 0".format(cost, 2))
    param5 = svm_parameter("-c {0} -t 1 -d {1} -g 1 -r 1 -h 0".format(cost, 5))
    m2 = svm_train(prob, param2)
    m5 = svm_train(prob, param5)
    eout2 = get_err(feat_tst, lab_tst, m2)
    eout5 = get_err(feat_tst, lab_tst, m5)
    return {'eout2': eout2, 'eout5': eout5}

def prob6d():
    """ Output: {'eout5': 0.021226415094339646, 'eout2': 0.018867924528301883} """
    return ghost6d(1, 5)

def prob7():
    """ 
    Output: 
    100 runs: {0: 5, -1: 2, -4: 46, -3: 43, -2: 4} -4 wins
    400 runs: {0: 18, -1: 9, -4: 146, -3: 211, -2: 16} -3 wins
    1024 runs: {0: 40, -1: 28, -4: 400, -3: 514, -2: 42} -3 wins 
    """
    digits = (1, 5)
    x, y = get('features.train')
    feat, lab= one_vs_one(x, y, digits[0], digits[1])
    features = np.array(feat)
    labels = np.array(lab)
    n_rows = len(labels)
    n_train_rows = int(n_rows * 0.9)
    np.random.seed()
    n_runs = 1024
    n_wins = dict(zip(range(-4, 1), [0] * 5))
    for j in range(n_runs):
        bestexval = 1.0
        winner = -5
        perm = np.random.permutation(n_rows)
        trainmask = (perm < n_train_rows)
        xvalmask = (perm >= n_train_rows)
        xtrain = features[trainmask].tolist()
        ytrain = labels[trainmask].tolist()
        xxval = features[xvalmask].tolist()
        yxval = labels[xvalmask].tolist()
        prob = svm_problem(ytrain, xtrain)
        for i in range(-4, 1):
            cost = 10**i
            param = svm_parameter("-c {0} -t 1 -d 2 -g 1 -r 1 -h 0".format(cost))
            m = svm_train(prob, param)
            exval = get_err(xxval, yxval, m)
            if exval < bestexval:
                winner = i
                bestexval = exval
        n_wins[winner] += 1
    print n_wins

def prob8():
    """ 
    Output: 
    100 runs: 0.00515923566879
    200 runs: 0.00471337579618
    512 runs: 0.00468998805732
    """
    digits = (1, 5)
    x, y = get('features.train')
    feat, lab = one_vs_one(x, y, digits[0], digits[1])
    features = np.array(feat)
    labels = np.array(lab)
    n_rows = len(labels)
    n_train_rows = int(n_rows * 0.9)
    np.random.seed()
    n_runs = 512
    ecv_total = 0.0
    for j in range(n_runs):
        perm = np.random.permutation(n_rows)
        trainmask = (perm < n_train_rows)
        xvalmask = (perm >= n_train_rows)
        xtrain = features[trainmask].tolist()
        ytrain = labels[trainmask].tolist()
        xxval = features[xvalmask].tolist()
        yxval = labels[xvalmask].tolist()
        prob = svm_problem(ytrain, xtrain)
        cost = 10**-3
        param = svm_parameter("-c {0} -t 1 -d 2 -g 1 -r 1 -h 0".format(cost))
        m = svm_train(prob, param)
        ecv_total += get_err(xxval, yxval, m)
    print ecv_total / n_runs

def prob9(digits=(1, 5)):
    """ Output: (6, 0.0006406149903908087) """
    x, y = get('features.train')
    feat, lab = one_vs_one(x, y, digits[0], digits[1])
    prob = svm_problem(lab, feat)
    lowest_ein = 1.0
    choice = -4
    for i in range(-2, 7, 2):
        cost = 10**i
        param = svm_parameter("-c {0} -t 2 -g 1.0 -h 0".format(cost))
        m = svm_train(prob, param)
        ein = get_err(feat, lab, m)
        print("ein for C={0}: {1}".format(cost, ein))
        if ein < lowest_ein:
            lowest_ein = ein
            choice = i
    return choice, lowest_ein

def prob10(digits=(1, 5)):
    """ Output: (2, 0.018867924528301883) """
    xtrain, ytrain = get('features.train')
    xtst, ytst = get('features.test')
    feattrain, labtrain = one_vs_one(xtrain, ytrain, digits[0], digits[1])
    feattst, labtst = one_vs_one(xtst, ytst, digits[0], digits[1])
    prob = svm_problem(labtrain, feattrain)
    lowest_eout = 1.0
    choice = -4
    for i in range(-2, 7, 2):
        cost = 10**i
        param = svm_parameter("-c {0} -t 2 -g 1.0 -h 0".format(cost))
        m = svm_train(prob, param)
        eout = get_err(feattst, labtst, m)
        print("eout for C={0}: {1}".format(cost, eout))
        if eout < lowest_eout:
            lowest_eout = eout
            choice = i
    return choice, lowest_eout

