#!/Users/vishnu/anaconda/bin/python

import random
import sys

"""class schema:

	files=[]

	def __init__(self):
		pass

	def addFile(self,file):
		self.files.append(file)

	def setForeignKey(self,primaryFile,theOtherOne):
		pass"""


class JoinReq:

	def __init__(self,R,S,m,n,fing):
		self.cost=0
		self.first_req=True

		self.cost = 0
		tC,self.t1=R.getFirst(m)
		#self.cost += tC
		tC,self.t2=S.getFirst(n)
		#self.cost += tC
		self.first_req==False
		self.R=R
		self.S=S
		self.m=m
		self.n=n
		self.fing=fing


	def pull(self):
		if self.fing==False:
			temp=""
			while self.t1 is not None:

				#print str(t1[m]) + "=" + str(t2[n])
				#print "x"
				while self.t2 is not None:
					#print str(self.t1[self.m]) + "=" + str(self.t2[self.n])
					if self.t1[self.m]==self.t2[self.n]:
						#self.emit((self.t1,self.t2))
						
						temp= (self.t1,self.t2)
						self.t2=self.S.getNext(self.n)
						self.cost+=1
						return temp

					self.t2=self.S.getNext(self.n)
					self.cost+=1


				#print "vishnu"
				self.t1=self.R.getNext(self.m)
				self.cost+=1

				#print str(t1) + "xx"
				#if t2==None:
				tC,self.t2=self.S.getFirst(self.n)
				self.cost+=tC
			return "eoo"
		else:
			"""savedLastKey=-1
			while self.t1 is not None:
				if self.t1>=savedLastKey:
					while self.t2 is not None:
						if self.t1[self.m]==self.t2[self.n]:
							#self.emit((self.t1,self.t2))
						
							temp= (self.t1,self.t2)
							self.t2=self.S.getNext(self.n)
							self.cost+=1
							return temp
						self.t2=self.S.getNext(self.n)
						self.cost+=1
				else:
					tC,self.t2=self.S.getFirst(self.n)
					self.cost+=tC

					while self.t2 is not None:
						if self.t1[self.m]==self.t2[self.n]:
							#self.emit((self.t1,self.t2))
						
							temp= (self.t1,self.t2)
							self.t2=self.S.getNext(self.n)
							self.cost+=1
							return temp

						self.t2=self.S.getNext(self.n)
						self.cost+=1


				savedLastKey=self.t1

				self.t1=self.R.getNext(self.m)
				self.cost+=1
			return "eoo" """

			savedLastKey=-1

			while self.t1 is not None:


				while self.t1 is not None: 			
					while self.t2 is not None and self.t1[self.m]>=self.t2[self.n]:
						#print str(self.t1[self.m]) + "=" + str(self.t2[self.n])
						if self.t1[self.m]==self.t2[self.n]:
						#self.emit((self.t1,self.t2))
							temp= (self.t1,self.t2)
							self.t2=self.S.getNext(self.n)
							self.cost+=1
							return temp
							
						self.t2=self.S.getNext(self.n)
						self.cost+=1

					if self.t2 is None:
						#print "t2 go non"
						while self.t1 is not None:
							self.t1=self.R.getNext(self.m)
							self.cost+=1
							if savedLastKey>self.t1[self.m]:
								tC,self.t2=self.S.getFirst(self.n)
								#print tC
								self.cost+=tC
								break
							
					if self.t2[self.n]>self.t1[self.m]:
						break

				while self.t2 is not None: 			
					while self.t1 is not None and self.t2[self.n]>=self.t1[self.m]:
						#print str(self.t1[self.m]) + "=" + str(self.t2[self.n])
						if self.t1[self.m]==self.t2[self.n]:
						#self.emit((self.t1,self.t2))
							temp= (self.t1,self.t2)
							self.t2=self.S.getNext(self.n)
							self.cost+=1
							return temp
						
						savedLastKey=self.t1[self.m]
						self.t1=self.R.getNext(self.m)
						self.cost+=1

						if self.t1 is None:
							return "eoo"
						if savedLastKey>self.t1[self.m]:
							tC,self.t2=self.S.getFirst(self.n)
							#print tC
							self.cost+=tC
							#print self.t2

					if self.t1[self.m]>self.t2[self.n]:
						break
			return "eoo"


	def getCost(self):
		return self.cost


class Xf:
	#max=25
	#data={}
	#stats  size,columns,runs,fingers,pkey,max,range
	#stats=(size,columns,runs,fingers,pkey,max,range)
	#stats={}
	#stats = {}

	def __init__(self,name):
		self.stats={}
		self.max=25
		self.keyCol=None
		self.stats["Name"]=name
		self.data={}
		self.setStats(0,0,0,0,0,0,0)
		pass

	def setStats(self,size,columns,runs,fingers,ordered,pkey,max):   #set the status values
		#print self 
		#print type(self.stats)
		self.stats["size"]=size
		self.stats["keyCol"]=pkey
		self.stats["max"]=max
		self.stats["columns"]=columns
		self.stats["runs"]=runs
		self.stats["cursors"]=[0 for x in range(columns)]

		self.keyCol=self.stats["keyCol"]
		self.max=self.stats["max"]
		self.stats["fingers"]=fingers
		self.stats["ordered"]=ordered
		self.fingers=fingers
		pass

	def sortCol(self):
		pass

	def reset(self):
		self.stats["fingers"]=[0 if x!=-1 else x for x in self.stats["fingers"]]


	def getSize(self):
		return int(self.stats["size"])

	def getRuns(self,col):
		return int(self.stats["runs"][col])


	def getFirst(self,col):
		tuple1 =[]
		for col in range(self.stats["columns"]):
			tuple1.append(self.data[str(col)][0])

		#print str(self.stats["fingers"][col]) + "*"

		tCost = self.stats["fingers"][col]
		#print tCost
		self.stats["fingers"][col]=0

		#if self.stats["Name"] == "s":
		#print "getFrist " + self.stats["Name"] + str(tuple1[col])
		return tCost, tuple1
		pass

	def getNext(self,col):

		#print self
		fingerPos=self.stats["fingers"][col]
		#print str(fingerPos) + "-" + str(len(self.data[str(0)])-2)

		if int(fingerPos)>=(len(self.data[str(col)])-2):
			#self.stats["fingers"][col]=0
			#print "yo"
			return None

		if self.stats["fingers"][col]!=-1 :
			self.stats["fingers"][col]+=1

		#print self.stats["fingers"][col]
		

		tuple1 =[]
		for col in range(self.stats["columns"]):
			tuple1.append(self.data[str(col)][fingerPos])

		#if self.stats["Name"] == "s":
		#print "getNext " + self.stats["Name"]+ str(tuple1[col])

		return tuple1
		pass

	def getFinger(self,col):
		return self.fingerPos

		pass

	def emit(self,x):
		#print "yo"
		#print x
                pass

	def eJoin(self,S,m,n):
		cost = 0
		tC,t1=self.getFirst(m)
		cost += tC
		tC,t2=S.getFirst(n)
		cost += tC

		while t1 is not None:
			#print str(t1[m]) + "=" + str(t2[n])
			#print "x"
			while t2 is not None:
				#print str(t1[m]) + "=" + str(t2[n])
				if t1[m]==t2[n]:
					self.emit((t1,t2))
				t2=S.getNext(n)
				cost+=1

			#print "vishnu"
			t1=self.getNext(m)
			cost+=1

			#print str(t1) + "xx"
			#if t2==None:
			tC,t2=S.getFirst(n)
			cost+=tC

		return cost
		pass

	def eJoin_pull(self,S,m,n):
		cost = 0
		tC,t1=self.getFirst(m)
		cost += tC
		tC,t2=S.getFirst(n)
		cost += tC

		while t1 is not None:
			#print str(t1[m]) + "=" + str(t2[n])
			#print "x"
			while t2 is not None:
				#print str(t1[m]) + "=" + str(t2[n])
				if t1[m]==t2[n]:
					self.emit((t1,t2))
				t2=S.getNext(n)
				cost+=1

			#print "vishnu"
			t1=self.getNext(m)
			cost+=1

			#print str(t1) + "xx"
			#if t2==None:
			tC,t2=S.getFirst(n)
			cost+=tC

		return cost
		pass

	#def __init__(self):
	#	self.data={}
	#	pass

	def __repr__(self):
		t1=""
		for key in self.data.keys():
			t1 = t1 + str(key) + " : " + str(self.data[key]) +"\n"
		
		t1= str(t1) + "\nprimary key: " + str(self.keyCol)

		return t1

	def setConstraints(self,key,max):		#there is some reduntant code here. Remove
		self.stats["keyCol"]=key
		self.keyCol=key
		self.max=max
		self.stats["max"]=max

		pass

	def printStats(self):
		print self.stats

	def replaceDupandSum(self,list1,list2):
		counter = 0 
		for i in range(len(list1)):
			counter=0
			for j in range(len(list2)):
				if list2[j]==list1[i]:
					#print "xx" + str(list2[j])
					#counter+=1
					#if counter>1:
					list2[j]=(list2[j]+list2[j+1])/2

		return list1+list2
		pass

	def FormData(self):
		"""		for col in range(self.cols):
			if col == self.keyCol:
				#print "key" + str(col)
				#print runs
				for r in range(self.runs[col]):
					temp=sorted(random.sample(range(self.max),size/runs[col]))
					#print temp
					self.data[str(col)]=self.replaceDupandSum(self.data.get(str(col),[]),temp)
				#self.data[str(col)]=set(self.data[str(col)])

				#print self.data[str(col)]


			else:
				for r in range(self.runs[col]):
					temp=sorted([random.randrange(self.max) for x in range(size/runs[col])])
					self.data[str(col)]=self.data.get(str(col),[])+temp"""

		self.Generate(self.stats["columns"],self.stats["runs"],self.stats["size"])


	def Generate(self,cols,runs,size):

		for col in range(cols):
			if col == self.keyCol:
				#print "key" + str(col)
				print runs
				for r in range(runs[col]):
					temp=sorted(random.sample(range(self.max),size/runs[col]))
					#print temp
					self.data[str(col)]=self.replaceDupandSum(self.data.get(str(col),[]),temp)
				#self.data[str(col)]=set(self.data[str(col)])
				#print self.data[str(col)]


			else:
				for r in range(runs[col]):
					temp=sorted([random.randrange(self.max) for x in range(size/runs[col])])
					self.data[str(col)]=self.data.get(str(col),[])+temp

			if self.stats["ordered"][col]==True:
				self.data[str(col)]=sorted(self.data[str(col)])

	def write2File(self,fileName):
		fp = open(fileName,'w')
		for col in range(cols):
			#print self.data[str(col)]
			stringD=""
			for x in self.data[str(col)]:
				stringD=stringD+" "+ str(x)
			fp.write(stringD+"\n")
		fp.close()
		pass

	def readFile(self,fileName):
		lines = open(fileName).read().splitlines()
		for x in range(cols):
			self.data[str(x)]=lines[0]
		pass



def nJoin(R,S,m,n):
	t1=R.getFirst(m)
	t2=S.getFirst(n)

	while t1 is not None:
		print str(t1[m]) + "=" + str(t2[n])
		#print "x"
		while t2 is not None:
			print str(t1[m]) + "=" + str(t2[n])
			if t1[m]==t2[n]:
				R.emit((t1,t2))
			t2=S.getNext(n)

		print "vishnu"
		t1=R.getNext(m)

		print str(t1) + "xx"
		#if t2==None:
		t2=S.getFirst(n)
	pass



#Generate(3,[3,3,3],9)

"""inst= file()
if len(sys.argv)>1:
	cols = int(sys.argv[1])
	runs = [int(x) for x in sys.argv[2:(len(sys.argv)-1)]]
	size = int(sys.argv[len(sys.argv)-1])


#print inst.replaceDupandSum([1,6,9,12],[2,5,6,11])


	inst.setConstraints(0,200000)
	inst.Generate(cols,runs,size)
	inst.write2File("file.txt")

	"""
#inst2=file()
#inst2.readFile("file.txt")
#print inst2
"""
inst3=Xf("r")



inst3.setStats(10,2,(2,3),[-1,0],0,40)
inst3.FormData()


inst4=Xf("s")
inst4.setStats(20,2,(2,3),[-1,0],0,40)
inst4.FormData()

print inst3
print inst4
"""

#print inst3.getFirst(1)
#print inst4.getFirst(1)

#print inst3.getNext(1)
#print inst4.getNext(1)


#print inst3.getNext(1)
#print inst4.getNext(1)


#nJoin(inst3,inst4,1,1)

#print inst3.eJoin(inst4,1,1)

"""
inst3.printStats()

print inst3.getFirst()

print inst3.getNext(1)
print inst3.getNext(1)
print inst3.getNext(1)
print inst3.getNext(1)
print inst3.getNext(1)"""





#print inst
