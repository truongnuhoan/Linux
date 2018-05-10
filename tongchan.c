#include <stdio.h>

void tongchan(int n)
{
	int i,tong = 0;
	for(i = 1;i <= n;i ++)
	{
		if( i%2 == 0)
		tong = tong+i;
	}
	printf("tong cac phan tu chan cua %d:%d",n,tong);
}
