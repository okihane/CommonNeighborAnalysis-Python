import numpy as np
#choose structure
type = 'a15'
def choose(type):
	if type == 'a15':
		lines = open("nb3sn3x3.lmp").readlines()
		numneighbor = 15
		cline = lines[122].split()#Nn14 125 120 122 130
	elif type == 'ico':
		lines = open("nb3sn3x3.lmp").readlines()
		numneighbor = 13
		cline = lines[127].split()#Sn12 127
	elif type == 'fcc':
		lines = open("fcc12.lmp").readlines()
		numneighbor = 13
		cline = lines[264].split()#264
	elif type == 'hcp':
		lines = open("hcp12.lmp").readlines()
		numneighbor = 13
		cline = lines[141].split()#141
	elif type == 'bcc':
		lines = open("bcc14.lmp").readlines()
		numneighbor = 15
		cline = lines[130].split()#130
	return lines, numneighbor, cline
def getneighbor(lines,cline):
	center = [float(cline[2]),float(cline[3]),float(cline[4])]
	sequence = np.array([])
	for i in range(16, len(lines)):
		linesi = lines[i].split()
		d = np.sqrt((float(linesi[2])-center[0])**2 + (float(linesi[3])-center[1])**2 + (float(linesi[4])-center[2])**2)
		a = np.array([d, float(linesi[2]), float(linesi[3]), float(linesi[4]), float(linesi[1]), float(linesi[0])])
		if len(sequence)<15:
			sequence = np.append(sequence, a).reshape(-1, 6)
		else:
			sequence = sequence[sequence[:,0].argsort()]
			if d<sequence[-1,0]:
				sequence[-1] = a
	localCutoff = np.sum(sequence[:,0]) / 14 * (1.0 + np.sqrt(2.0)) * 0.5
	return sequence, localCutoff
def dd(x1,x2):
    return np.sqrt((x1[1]-x2[1])**2 + (x1[2]-x2[2])**2 + (x1[3]-x2[3])**2)
#common
# nn = 15
def comm(nn,sequence,localCutoff):
	common = []
	comseqs = []
	for ni1 in range(1,nn):
		comseq = []
		temp = 0
		for ni2 in range(1,nn):
			if ni1 != ni2:
				if dd(sequence[ni1],sequence[ni2]) <= localCutoff:
					temp += 1
					comseq.append(ni2)
					#comseq.append(sequence[ni2])
		common.append(temp)
		comseqs.append(comseq)
	return common,comseqs
#bond
def countbond2(seqs):
	bonds = []
	bondpairs = []
	for i3 in range(len(seqs)):
		tempbond = 0
		tempbondpair = []
		for i4 in range(len(seqs[i3])):
			t = seqs[i3][i4]
			b = np.intersect1d(seqs[i3],seqs[t-1])
			if i4 != 0:
				for i5 in range(i4):
					if np.isin(seqs[i3][i5],b):
						tempbond += 1
						tempbondpair.append([seqs[i3][i5],t])
		bonds.append(tempbond)
		bondpairs.append(tempbondpair)
	return bonds,bondpairs
#chain
class Chain:
	def __init__(self,pair):
		self.pair = np.array(pair)
		self.tempair = pair[0]
		self.left = 0
		self.right = 0
		self.lianchang = 0
		self.totalong = 0
		self.lian = []
		self.alllian = []

	def leftsearch(self):
		lflag = False
		for li in range(len(self.tempair)):
			cellpair = self.tempair[li]
			if cellpair.size > 0:
				if np.intersect1d(self.left,cellpair):
					if cellpair[0]==self.left:
						self.left = cellpair[1]
					else:self.left = cellpair[0]
					self.tempair = np.delete(self.tempair,li,axis=0)
					self.lianchang += 1
					self.totalong -= 1
					# print(self.totalong)
					if self.totalong > 0:
						lflag = True
					break
		if lflag:
			self.leftsearch()
	def rightsearch(self):
		# print('hhhhh'+str(self.totalong))
		if self.totalong==0:
			self.lian.append(self.lianchang)
			# print(self.lian)
			return
		rflag = False
		for ri in range(len(self.tempair)):
			cellpair = self.tempair[ri]
			if cellpair.size > 0:
				if np.intersect1d(self.right,cellpair):
					if cellpair[0]==self.right:
						self.right = cellpair[1]
					else:self.right = cellpair[0]
					self.tempair = np.delete(self.tempair,ri,axis=0)
					self.lianchang += 1
					self.totalong -= 1
					rflag = True
					break
		if rflag:
			self.rightsearch()
		else:
			self.lian.append(self.lianchang)
			#print(lian)
	
	def start(self):
		#for tempair in pair:
		for i1 in range(len(self.pair)):
			self.tempair = np.array(self.pair[i1])
			if len(self.tempair) > 0:
				self.tempair = self.tempair[self.tempair[:,0].argsort()]
				self.totalong = len(self.tempair)
				self.lian = []
				self.lianchang = 1
				while self.totalong>0:
					self.left = self.tempair[0][0]
					self.right = self.tempair[0][1]
					self.tempair = np.delete(self.tempair,0,axis=0)
					self.totalong -= 1
					self.leftsearch()
					self.rightsearch()
				self.alllian.append(np.amax(self.lian))
			else: self.alllian.append(0)
		return self.alllian
if __name__ == '__main__':
	lines, numneighbor, cline = choose(type)
	sequence, localCutoff = getneighbor(lines,cline)
	common,comseqs = comm(numneighbor,sequence,localCutoff)
	bond,bondpair = countbond2(comseqs)
	maxchain = Chain(bondpair)
	alllians = maxchain.start()
	# print(localCutoff)
	print(common)
	print(bond)
	print(alllians)
