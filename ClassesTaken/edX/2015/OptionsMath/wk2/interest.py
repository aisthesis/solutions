"""
Solutions to wk 2 homework from 
CaltechX: BEM1105x Pricing Options with Mathematical Models
https://courses.edx.org/courses/CaltechX/BEM1105x/1T2015/info

Copyright (c) 2015 Marshall Farrier
"""

import math

import pynance as pn

def prob2pract():
    pv1 = _prob2helper(5000., 4500., 7000., 1.02)
    pv2 = _prob2helper(5500., 5000., 9000., 1.02)
    return pv1, pv2, pv1 - pv2

def prob2real():
    pv1 = _prob2helper(6000., 5500., 9000., 1.01)
    pv2 = _prob2helper(6500., 6000., 11000., 1.01)
    return pv1, pv2, pv1 - pv2

def _prob2helper(pmt1, installments, repayment, qtrlygrowth):
    return pmt1 + installments / qtrlygrowth + installments / qtrlygrowth**2 - repayment / qtrlygrowth**8

def _helper3(loan, yrs, apr, nomrate):
    _monthly_apr = pn.interest.loanpayment(loan, apr / 12., yrs * 12)
    _pvnom = pn.interest.pvannuity(nomrate / 12., yrs * 12) * _monthly_apr
    return _monthly_apr, _pvnom, _pvnom - loan

def prob3pract():
    return _helper3(50000., 15, .09, .085)

def prob3real():
    return _helper3(500000, 30, .066, .06)

def prob4pract():
    return _helper4(4., 104., 102., 98.2)

def prob4real():
    _r1yr = _helper4(5., 105., 104., 98.)
    return 100. / (1. + _r1yr)

def _helper4(coupon, face1yr, price1yr, price6mo):
    _gr6 = 100. / price6mo
    _pvcoup = coupon / _gr6
    _pvface = price1yr - _pvcoup
    return face1yr / _pvface - 1.

def prob5pract():
    return _helper5(96, 1, 85, 3) - 1.

def prob5real():
    return _helper5(98, 1, 90, 4) - 1.

def _helper5(price1, yrs1, price2, yrs2):
    """ return interim forward rate """
    return (float(price1) / price2)**(1. / (yrs2 - yrs1))
