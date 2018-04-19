n = input ('n=')
#in ra cac so tu 1 den n
for i in range (1,n+1):
     print i
#in ra tong cac so chan
s = 0
for i in range (1,n+1):
     if(i%2 == 0):
        s = s+i
	print 'tong cac so chan = ',s
