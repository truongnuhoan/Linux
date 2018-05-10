class hcn:
	'tinh chu vi, dien tich hinh chu nhat'
	dai = ''
	rong = ''
	def __init__(self,dai,rong):
		self.dai = dai
		self.rong = rong
	def getchuvi(self):
		return (self.dai + self.rong)*1.0/2
	def getdientich(self):
		return (self.dai * self.rong)
	def display(self):
		print 'dai = ',self.dai
		print 'rong = ',self.rong
		print 'CV = ',self.getchuvi()
		print 'DT = ',self.getdientich()
dodai = []
n = input ('n = ')
for i in range (0,n):
	print 'nhap hcn [',i+1,']'
	dodai.append(hcn(input('dai = '),input('rong = ')))
print '\n mang vua nhap :'
for i in range (0,n):
	print '\n hcn [',i+1,']:'
	dodai[i].display()

	




