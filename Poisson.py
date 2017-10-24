#Poisson Calculator
#Equation from Intro to Genetic Analysis 6th Edition
#Clay Ludwig

import math
import sys

MVal = input('Average Event Rate ')
IVal = input('i Value / Event Occurence ')

NegM = float(MVal * -1)
EPowNegM = float(math.e ** NegM)
MPowI = float(MVal ** IVal)
TopTotal = float(EPowNegM * MPowI)
IFac = float(math.factorial(IVal))
FVal = float(TopTotal / IFac)


infoMessage = 'Value = ' + repr(round(FVal,5))
print(infoMessage)
