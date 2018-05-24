class HangHoa:
	'lop Hang Hoa'
	MaHH = ''
	TenHH = ''
	GiaBan = ''
	def __init__(self,MaHH,TenHH,GiaBan):
		self.MaHH = MaHH
		self.TenHH = TenHH
		self.GiaBan = GiaBan
	def display(self):
		print 'Ma Hang Hoa = ',self.MaHH
		print 'Ten Hang Hoa = ',self.TenHH
		print 'Gia Ban = ',self.GiaBan
HH= []
n = input ('n = ')
for i in range (0,n):
	print 'nhap HH [',i+1,']'
	HH.append(HangHoa(input('Ma Hang Hoa = '),input('Ten Hang Hoa = '), input('Gia Ban = ')))
print '\n mang vua nhap :'
for i in range (0,n):
	print '\n hcn [',i+1,']:'
	HH[i].display()
x = input ('X = ')
print '\n thong tin mat hang co ma ',x,': \n'
for i in range (0,n):
	if (HH[i].MaHH == x):
		HH[i].display()
		break
	if(i == n-1):
		print 'Mat hang khong ton tai\n'

