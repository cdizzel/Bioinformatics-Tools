#Map Distance Calculator
#Equation from Hilgardia Vol.24 no.10 Allard R. W.
#Clay Ludwig
#This program outputs to a CSV file in this files directory

import math
import sys

#Add some class into text. Really gotta class the place up

ExitInfo = 'To exit this program hit 1 then enter'
RegularInfo = 'This code can handle values between 0 and .5.'
CSVInfo = 'This program will save values to a CSV file by default'
print(RegularInfo)
print(CSVInfo)
print(ExitInfo)

#this block handles file name setup and initial formatting
FOName = raw_input('Please input CSV output name without ".csv" \n')
FOName = FOName + str('.csv')
fo = open(FOName, "a+")
fo.write('Input Value');
fo.write(",");
fo.write('Relative Frequency');
fo.write('\n');
fo.close()

print('Please input RF values')

def CMDistance(RF):	#the mathey bits
	Var2Rf = float(2*(RF))
	Var1Min2Rf = float(1 - Var2Rf)
	VarLog = math.log(Var1Min2Rf)
	CM = (-50 * VarLog)
	infoMessage = 'Corrected Map Distance for Value ' + repr(RF) + ' = ' + repr(round(CM,4))
	print(infoMessage)
	return CM

def CSVSave(InVal, RFVal):	#CSV dump
	fo = open(FOName, "a+")
	fo.write(str(InVal));
	fo.write(",");
	fo.write(str(RFVal));
	fo.write('\n');
	fo.close()

while (1):	#This section keeps the whole mess running
	RF1 = input('RF ')
	if (RF1 == 1):
		sys.exit(0)
	CM = CMDistance(RF1)
	CSVSave(RF1, CM)
