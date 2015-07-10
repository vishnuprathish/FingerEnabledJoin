from fingered import *
import random
import csv
import sys
from plotgraph import *

def run():
	records = random.randrange(200, 5000)
	inst3=Xf("r")
	inst3.setStats(records,2,(2, random.randrange(50, 2999)),[-1,0],[False,False],0,100000, records)
	inst3.FormData()

	inst4=Xf("s")
	inst4.setStats(records,2,(1,1),[-1,0],[False,True],0,100000, records)
	inst4.FormData()

	print inst3
	print inst4

	#pCost = inst3.getSize() + (inst4.getSize() * inst3.getRuns(1) )+ (inst3.getRuns(1) * inst4.getSize())
	pCost = inst3.getSize() + inst4.getSize() * inst3.getRuns(1) 

	systermRcost = inst3.getSize() + inst4.getSize() * inst3.getSize() 
	#pCost = 0.6 * pCost

	j=JoinReq(inst3,inst4,1,1,True)

	tup=j.pull()
	while tup is not "eoo":
		#print str(tup)

		tup=j.pull()


	print "\nNested Loop Join:\n"

	inst3.reset()
	inst4.reset()
	k=JoinReq(inst3,inst4,1,1,False)

	tup=k.pull()
	while tup is not "eoo":
		tup=k.pull()

	

	print "Summary:"
	print "selected file1size: " + str(records)
	print "selected number of runs for file1: " + str(inst3.getRuns(1))
	print "Predicted Cost Finger:" + str(pCost)
	print "Actual Cost Finger:" + str(j.getCost())
	print "Actual cost of nested loop: "  + str(k.getCost()) 
	#print "Actual Cost NLJ:" + str(k.getCost())

	#print "("+ str(records) +","+ str(inst3.getRuns(1)) +","+ str(inst4.getSize()) +","+ str(pCost) +","+ str(j.getCost())+")"

	#tup = [ str(records), str(inst3.getRuns(1)),str(inst4.getSize()),str(pCost),str(j.getCost())]
	#print tup

	return pCost, j.getCost(), k.getCost(), systermRcost, records


	#fp = open("toexcel.csv","ab")

	#writer = csv.writer(fp)
	#data = [tup]
	#writer.writerows(data)


arrPredicted = []
arrActual = []
arrSize = []
arrNested = []
arrsysR = []

for i in range(2000):
	predicted, actual, nested, sysR, size = run()
	arrPredicted.append(predicted)
	arrActual.append(actual)
	arrSize.append(size * size)
	arrNested.append(nested)
	arrsysR.append(sysR)


print arrActual
print arrPredicted
chartPlot3(sorted(arrsysR), sorted(arrNested), sorted(arrSize), "System R Cost equation", "Nested loop Empirical cost", "SysR vs Nested")
chartPlot3(sorted(arrsysR), sorted(arrActual), sorted(arrSize), "System R Cost equation", "Finger enabled empirical cost", "SysR vs Finger")
chartPlot3(sorted(arrPredicted), sorted(arrActual), sorted(arrSize), "Predicted cost using new cost formula", "Finger enabled empirical cost", "New vs finger")


#chartPlot3(sorted(arrActual), sorted(arrPredicted), sorted(arrSize))
#plot4(sorted(arrActual), sorted(arrPredicted), sorted(arrNested), sorted(arrSize))
#plot5(sorted(arrActual), sorted(arrPredicted), sorted(arrNested), sorted(arrsysR), sorted(arrSize))


