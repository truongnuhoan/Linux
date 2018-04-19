class dl :
	'Bang Du lIEU Sinh Vien'
	MSSV =''
	HoTen =''
	MaKhoa = ''
	def __init__(self,MSSV,HoTen,MaKhoa):
		self.MSSV = MSSV
		self.HoTen = HoTen
		self.MaKhoa = MaKhoa
	def display(self):
	    print self.MSSV, self.HoTen, self.MaKhoa
x = dl('MSSV','Ho Ten', 'Ma Khoa')
x.display()
sv = []
sv.append(dl('001','Mai A','01'))
sv.append(dl('002','Tran B','01'))
sv.append(dl('003','Van C','02'))
sv.append(dl('004','Thi K','01'))

for a in sv:
	a.display()
#lop khoa
class khoa:
	'Bang Du Lieu Khoa'
	TenKhoa =''
	MaKhoa = ''
	def __init__(self,MaKhoa,TenKhoa):
		self.MaKhoa = MaKhoa
		self.TenKhoa = TenKhoa
	def display(self):
	    print self.MaKhoa, self.TenKhoa
y= khoa('Ma Khoa', 'Ten Khoa')
y.display()
k = []
k.append(khoa('01','CNTT'))
k.append(khoa('02','Ke Toan'))
k.append(khoa('03','Co Khi'))
k.append(khoa('04','Nuoi'))

for b in k:
	b.display()
print 'sinh vien thuoc khua CNTT'
for a in sv:
	for b in k:
		if(a.MaKhoa == b.MaKhoa):
		   if(b.MaKhoa == '01'):
			print a.HoTen




	
	
	
