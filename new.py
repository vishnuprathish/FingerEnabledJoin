from fingered import *
import random
import csv
import sys
from plotgraph import *
import time

def run():
	records = random.randrange(200, 1000)
	inst3=Xf("r")
	inst3.setStats(records,2,(2, random.randrange(50, 200)),[-1,0],[False,False],0,100000, 0.3 * records)
	inst3.FormData()

	inst4=Xf("s")
	inst4.setStats(records,2,(1,1),[-1,0],[False,True],0,100000, 0.3 * records)
	inst4.FormData()

	start_time = time.time()
	pCost = inst3.getSize() + inst4.getSize() * inst3.getRuns(1) 
	pTime = time.time() - start_time

	pTime = float(pCost) / 1000000 * float(0.5)

	start_time = time.time()
	systermRcost = inst3.getSize() + inst4.getSize() * inst3.getSize() 
	systermRTime = time.time() - start_time

	systermRTime = float(systermRcost) / 1000000 * float(0.5)

	start_time = time.time()
	j=JoinReq(inst3,inst4,1,1,True)
	tup=j.pull()
	while tup is not "eoo":
		tup=j.pull()
	jTime = time.time() - start_time

	print "\nNested Loop Join:\n"

	inst3.reset()
	inst4.reset()
	start_time = time.time()
	k=JoinReq(inst3,inst4,1,1,False)
	tup=k.pull()
	while tup is not "eoo":
		tup=k.pull()
	kTime = time.time() - start_time

	

	print "Summary:"
	print "selected file1size: " + str(records)
	print "selected number of runs for file1: " + str(inst3.getRuns(1))
	print "Predicted Cost Finger:" + str(pCost)
	print "Actual Cost Finger:" + str(j.getCost())
	print "Actual cost of nested loop: "  + str(k.getCost()) 

	return pCost, pTime, j.getCost(), jTime, k.getCost(), kTime, systermRcost, systermRTime, records


	#fp = open("toexcel.csv","ab")
	#writer = csv.writer(fp)
	#data = [tup]
	#writer.writerows(data)


arrPredicted = []
arrActual = []
arrSize = []
arrNested = []
arrsysR = []

arrPredictedTime = []
arrActualTime = []
arrNestedTime = []
arrsysRTime = []

for i in range(20):
	predicted, pT, actual, aT, nested,nT, sysR, sT, size = run()
	arrPredicted.append(predicted)
	arrActual.append(actual)
	arrSize.append(size * size)
	arrNested.append(nested)
	arrsysR.append(sysR)

	arrPredictedTime.append(pT)
	arrActualTime.append(aT)
	arrNestedTime.append(nT)
	arrsysRTime.append(sT)

arrPredictedTime = [float(pC) / 1000000 * float(max(arrActualTime)-min(arrActualTime)) for pC in arrPredicted]
arrsysRTime = [float(pT) / 1000000 * float(max(arrNestedTime)-min(arrNestedTime)) for pT in arrsysR]

chartPlot3(sorted(arrsysR), sorted(arrNested), sorted(arrSize), "System R Cost equation", "Nested loop Empirical cost", "SysR vs Nested")
chartPlot3(sorted(arrsysR), sorted(arrActual), sorted(arrSize), "System R Cost equation", "Finger enabled empirical cost", "SysR vs Finger")
chartPlot3(sorted(arrPredicted), sorted(arrActual), sorted(arrSize), "Predicted cost using new cost formula", "Finger enabled empirical cost", "New vs finger")

chartPlot3(sorted(arrsysRTime), sorted(arrNestedTime), sorted(arrSize), "System R Cost equation", "Nested loop Empirical cost", "SysR vs NestedT", max(arrsysRTime))
chartPlot3(sorted(arrsysRTime), sorted(arrActualTime), sorted(arrSize), "System R Cost equation", "Finger enabled empirical cost", "SysR vs FingerT", max(arrsysRTime))
chartPlot3(sorted(arrPredictedTime), sorted(arrActualTime), sorted(arrSize), "Predicted cost using new cost formula", "Finger enabled empirical cost", "New vs fingerT", max(arrsysRTime))
#dataDist(arrSize)


#chartPlot3(sorted(arrActual), sorted(arrPredicted), sorted(arrSize))
#plot4(sorted(arrActual), sorted(arrPredicted), sorted(arrNested), sorted(arrSize))
#plot5(sorted(arrActual), sorted(arrPredicted), sorted(arrNested), sorted(arrsysR), sorted(arrSize))


