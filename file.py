import random
import sys

class schema:

	files=[]

	def __init__(self):
		pass

	def addFile(self,file):
		self.files.append(file)

	def setForeignKey(self,primaryFile,theOtherOne):
		pass


class file:
	keyCol=None
	max=25
	data={}



	#stats  size,columns,runs,fingers,pkey,max,range

	#stats=(size,columns,runs,fingers,pkey,max,range)
	stats={}

	def setStats(self,size,columns,runs,fingers,pkey,max):   #set the status values 
		self.stats["size"]=size
		self.stats["keyCol"]=pkey
		self.stats["max"]=max
		self.stats["columns"]=columns
		self.stats["runs"]=runs
		self.stats["cursors"]=[0 for x in range(columns)]


		self.keyCol=self.stats["keyCol"]
		self.max=self.stats["max"]
		self.stats["fingers"]=fingers
		self.fingers=fingers

		pass


	def getVal(self,col,idx):
		return self.data[str(col)][idx]


	def getFirst(self,col):
		tuple1 =[]
		for col in range(self.stats["columns"]):
			tuple1.append(self.data[str(col)][0])

		self.stats["fingers"][col]=0

		return tuple1
		pass

	def getNext(self,col):
		fingerPos=self.stats["fingers"][col]
		print str(fingerPos) + "-"

		
		if self.stats["fingers"][col]!=-1 :
			self.stats["fingers"][col]+=1

		print self.stats["fingers"][col]
		print str(self.stats["size"]) + " yy"

		if fingerPos>=len(self.data[str(0)])-1:
			#self.stats["fingers"][col]=0
			return None

		tuple1 =[]
		for col in range(self.stats["columns"]):
			tuple1.append(self.data[str(col)][fingerPos])


		

		return tuple1
		pass

	def emit(self,x):
		print "yo"
		print x

	def eJoin(self,S,m,n):
		t1=self.getFirst(m)
		t2=S.getFirst(n)

		while t1 is not None:
			print str(t1[m]) + "=" + str(t2[n])
			
			#print "x"

			while t2 is not None:
				print str(t1[m]) + "=" + str(t2[n])
				if t1[m]==t2[n]:
					self.emit((t1,t2))
				t2=S.getNext(n)

			t1=self.getNext(m)
			
			print str(t1) + "xx"
			#if t2==None:
			t2=S.getFirst(n)

		pass



	def __init__(self):
		self.data={}
		pass

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
				print runs
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

inst3=file()
inst3.setStats(10,2,(2,3),[-1,0],0,30)
inst3.FormData()


inst4=file()
inst4.setStats(20,2,(2,3),[-1,0],0,30)
inst4.FormData()

print inst3
print inst4

inst3.eJoin(inst4,1,1)

"""
inst3.printStats()

print inst3.getFirst()

print inst3.getNext(1)
print inst3.getNext(1)
print inst3.getNext(1)
print inst3.getNext(1)
print inst3.getNext(1)"""





#print inst