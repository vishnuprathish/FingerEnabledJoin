from fingered import *


inst3=Xf("r")
inst3.setStats(6000,2,(2,10),[-1,0],[False,False],0,40000)
inst3.FormData()


inst4=Xf("s")
inst4.setStats(3000,2,(2,3),[-1,0],[False,True],0,40000)
inst4.FormData()

print inst3
print inst4


print "Predicted Cost of Fingered Join from Stats: "

pCost = inst3.getSize() + (inst4.getSize() * inst3.getRuns(1) )+ (inst3.getRuns(1) * inst4.getSize())

print pCost

#print inst3.eJoin(inst4,1,1)


print "\n Fingered Join:"

j=JoinReq(inst3,inst4,1,1,True)


tup=j.pull()
while tup is not "eoo":
	print str(tup)

	tup=j.pull()

print "Cost : "  + str(j.getCost())



"""
print "\nNested Loop Join:\n"

inst3.reset()
inst4.reset()

j=JoinReq(inst3,inst4,1,1,False)


tup=j.pull()
while tup is not "eoo":
	print str(tup)

	tup=j.pull()

print "Cost : "  + str(j.getCost()) """


print "\n Summary:"
print "Predicted Cost:" + str(pCost)
print "Actual Cost:" + str(j.getCost())