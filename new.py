from fingered import *
import random
import csv
import sys
from plotgraph import *

def run():
	records = random.randrange(200, 1000)
	inst3=Xf("r")
	inst3.setStats(records,2,(2,40),[-1,0],[False,False],0,40000, 10)
	inst3.FormData()

	inst4=Xf("s")
	inst4.setStats(records,2,(1,1),[-1,0],[False,True],0,40000, 10)
	inst4.FormData()

	print inst3
	print inst4

	pCost = inst3.getSize() + (inst4.getSize() * inst3.getRuns(1) )+ (inst3.getRuns(1) * inst4.getSize())
	pCost = inst3.getSize() + (inst4.getSize() * inst3.getRuns(1) )+ (inst3.getRuns(1) * inst4.getSize())	
	#pCost = 0.6 * pCost


	j=JoinReq(inst3,inst4,1,1,True)

	tup=j.pull()
	while tup is not "eoo":
		#print str(tup)

		tup=j.pull()

	"""
	print "\nNested Loop Join:\n"

	inst3.reset()
	inst4.reset()

	k=JoinReq(inst3,inst4,1,1,False)


	tup=k.pull()
	while tup is not "eoo":
		print str(tup)

		tup=k.pull()

	print "Cost : "  + str(k.getCost()) 

	"""


	print "Summary:"
	print "selected file1size: " + str(records)
	print "selected number of runs for file1: " + str(inst3.getRuns(1))
	print "Predicted Cost Finger:" + str(pCost)
	print "Actual Cost Finger:" + str(j.getCost())
	#print "Actual Cost NLJ:" + str(k.getCost())

	print "("+ str(records) +","+ str(inst3.getRuns(1)) +","+ str(inst4.getSize()) +","+ str(pCost) +","+ str(j.getCost())+")"

	tup = [ str(records), str(inst3.getRuns(1)),str(inst4.getSize()),str(pCost),str(j.getCost())]
	print tup

	return pCost, j.getCost(), records


	#fp = open("toexcel.csv","ab")

	#writer = csv.writer(fp)
	#data = [tup]
	#writer.writerows(data)


arrPredicted = []
arrActual = []
arrSize = []

for i in range(200):
	predicted, actual, size = run()
	arrPredicted.append(predicted)
	arrActual.append(actual)
	arrSize.append(size + size)


print arrActual
print arrPredicted
#chartPlot3(arrActual, arrPredicted, arrSize)
chartPlot3(sorted(arrActual), sorted(arrPredicted), sorted(arrSize))


