#include <stdio.h>

void luythua(int a,int n)
{
	int i, kq = a;
	if (n == 1)
	printf(" luy thua bac 1 cua %d:%d",a,kq);
	else 
		for(i = 2;i <= n;i ++ )
		{
			kq = kq*a;		
		}
	printf("luy thua %d mu %d:%d",a,n,kq);
}
