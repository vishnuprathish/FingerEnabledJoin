#!/Users/vishnu/anaconda/bin/python

import random
import sys

class JoinReq:

	def __init__(self,R,S,m,n,fing):
		self.cost=0
		self.first_req=True

		self.cost = 0
		tC,self.t1=R.getFirst(m)
		tC,self.t2=S.getFirst(n)
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
				while self.t2 is not None:
					if self.t1[self.m]==self.t2[self.n]:						
						temp = (self.t1,self.t2)
						self.t2=self.S.getNext(self.n)
						self.cost+=1
						return temp
					self.t2=self.S.getNext(self.n)
					self.cost+=1
				self.t1=self.R.getNext(self.m)
				self.cost+=1
				tC,self.t2=self.S.getFirst(self.n)
			return "eoo"
		else:
			savedLastKey=-1

			while self.t1 is not None:
				while self.t1 is not None: 			
					while self.t2 is not None and self.t1[self.m]>=self.t2[self.n]:
						if self.t1[self.m]==self.t2[self.n]:
							temp = (self.t1, self.t2)
							self.t2=self.S.getNext(self.n)
							self.cost+=1
							return temp
							
						self.t2=self.S.getNext(self.n)
						self.cost+=1

					if self.t2 is None:
						while self.t1 is not None:
							self.t1=self.R.getNext(self.m)
							if self.t1 == None:
								break
							self.cost+=1
							if savedLastKey>self.t1[self.m]:
								tC,self.t2=self.S.getFirst(self.n)
								break
					
					if self.t1 == None:
						break		
					if self.t2[self.n]>self.t1[self.m]:
						break

				while self.t2 is not None: 			
					while self.t1 is not None and self.t2[self.n]>=self.t1[self.m]:
						if self.t1[self.m]==self.t2[self.n]:
							temp = (self.t1, self.t2)
							self.t2 = self.S.getNext(self.n)
							self.cost += 1
							return temp
						
						if self.t1[self.m] is not None:
							savedLastKey=self.t1[self.m]
						self.t1=self.R.getNext(self.m)
						self.cost+=1

						if self.t1 is None:
							return "eoo"
						if savedLastKey>self.t1[self.m]:
							tC,self.t2=self.S.getFirst(self.n)
					if self.t1[self.m]>self.t2[self.n]:
						break
			return "eoo"


	def getCost(self):
		return self.cost


class Xf:

	def __init__(self,name):
		self.stats={}
		self.max=25
		self.keyCol=None
		self.stats["Name"]=name
		self.data={}
		self.setStats(0,0,0,0,0,0,0, 0)
		self.keys = 0
		pass

	def setStats(self,size,columns,runs,fingers,ordered,pkey,max, keys):   #set the status values #fix keys ... same number of keys for every value
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
		self.keys = keys
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

		tCost = self.stats["fingers"][col]
		self.stats["fingers"][col]=0

		return tCost, tuple1
		pass

	def getNext(self,col):
		fingerPos=self.stats["fingers"][col]
		if int(fingerPos)>=(len(self.data[str(col)])-2):
			return None

		if self.stats["fingers"][col]!=-1 :
			self.stats["fingers"][col]+=1		

		tuple1 =[]
		for col in range(self.stats["columns"]):
			tuple1.append(self.data[str(col)][fingerPos])

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
		#cost += tC
		tC,t2=S.getFirst(n)
		#cost += tC

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
		#cost += tC
		tC,t2=S.getFirst(n)
		#cost += tC

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
			#cost+=tC

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
		self.Generate(self.stats["columns"],self.stats["runs"],self.stats["size"])


	def Generate(self,cols,runs,size):

		for col in range(cols):
			if col == self.keyCol:  #primary key not handled
				#print "key" + str(col)
				#print runs
				for r in range(runs[col]):
					temp=sorted(random.sample(range(self.max),size/runs[col]))
					#include add sufficient duplicates per run
					keys_per_run = self.keys/runs[col]
					duplicates_per_run = len(temp) - keys_per_run
					
					while duplicates_per_run > 0 :
					    random_pos = random.randrange(1, len(temp))
					    temp[random_pos - 1] = temp[random_pos]
					    duplicates_per_run = duplicates_per_run - 1
					
					self.data[str(col)]=self.data.get(str(col),[])+temp
			else:
				for r in range(runs[col]):
					temp=sorted([random.randrange(self.max) for x in range(size/runs[col])])
					self.data[str(col)]=self.data.get(str(col),[])+temp
					
			if self.stats["ordered"][col]==True:
				self.data[str(col)]=sorted(self.data[str(col)])

	def write2File(self,fileName):
		fp = open(fileName,'w')
		for col in range(cols):
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
		while t2 is not None:
			if t1[m]==t2[n]:
				R.emit((t1,t2))
			t2=S.getNext(n)

		t1=R.getNext(m)
		t2=S.getFirst(n)
	pass




