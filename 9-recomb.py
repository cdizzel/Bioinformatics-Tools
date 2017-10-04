#Recomb test for 9 variables
#Equation from Hilgardia Vol.24 no.10 Allard R. W.
#Clay Ludwig

import sys

p = 0.00001 #Add more zeros for more precision. Nah, jk. Please don't, that comes later.
iteration = 0 #but arrays start at 1
OldFVal = 1
FirstFval = 0

print('Please enter values for observed frequency')

FrE = input('AABB')
FrF = input('AaBB')
FrG = input('AABb')
FrHI = input('AaBb')
FrJ = input('AAbb')
FrK = input('Aabb')
FrL = input('aaBB')
FrM = input('aaBb')
FrN = input('aabb')

def the_math():
	V2Divp = float(2/p)
	pMul2 = float(p*2)
	V1Minp = float(1-p)
	pMin1 = float(p-1)
	FBA = float((2*(pMul2-1)))
	pSq = float(p*p)
	FBB1 = float(2*pSq)
	FBB = float((1-(2*p))+FBB1)
	FB = float(FBA/FBB)
	FtoM = float(FrF+FrG+FrK+FrM)
	FrJL = float(FrJ+FrL)
	FrEN = float(FrE+FrN)
	V1Min2p = float(1-pMul2)
	pMul1Minp = float(p*V1Minp)
	V2DivpMin1 = float(2/pMin1)


	Val = float(FrEN*V2Divp)+(FtoM*(V1Min2p/pMul1Minp)+(FrJL*V2DivpMin1)+(FrHI*FB))

	return Val

FVal = the_math() #run once to pass the "while" control 


while (FVal > .01 or FVal < 0): #any higher certainty than .001 causes the program to take its sweet time
	p = p + 0.00001
	FVal = the_math()
	iteration = iteration + 1
	ItNum = 'Iteration ' + repr(iteration)
	print (ItNum)
	print(FVal)

	if (iteration == 1):
		FirstFval = FVal
	if(p > 1): #should be 1. These things never need to go above 1.
		print('Error 0: Ya broke it. Invalid Output. Check your input data.')
		sys.exit(0)


while (OldFVal > FVal and FVal > 0):
	OldFVal = FVal
	p = p + 0.00000001
	FVal = the_math()
	iteration = iteration + 1
	ItNum = 'Iteration ' + repr(iteration)
	print (ItNum)
	print(FVal)


FVal = OldFVal #FVal goes 1 over non-zero limit

info = float((2*((1-(3*p))+(3*(p*p))))/((p*(1-p))*(1-(2*p)+(2*(p*p)))))

#Text Printouts
FinalVal = 'Final Value = ' + repr(FVal)
pFinal = 'P= ' + repr(p)
pRound = 'Rounded P = ' + repr(round(p,4))
ExitMessage = 'P values less than .5 correspond to coupling, higher values will be reformatted'
Accuracy = float(FVal / FirstFval)
AccuracyMessage = 'Accurate within ' + repr(Accuracy) + ' %'
infoMessage = 'Information Produced = ' + repr(round(info,4))
print('')
print('')
print('')
print(ExitMessage)
print('')
print(FinalVal)
print(AccuracyMessage)
print(pFinal)
print('')
print(pRound)
print(infoMessage)


if (p > .5):
	pRepulsion = (1 - p)
	pRepulMessage = 'Repulsion Value of ' + repr(round(pRepulsion,4))
	print(pRepulMessage)

#job well done team
sys.exit(0)