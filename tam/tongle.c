#include <stdio.h>

void tongle(int n)
{
	int i,tong = 0;
	for(i = 1;i < n;i ++)
	{
		if( i%2 ==1 )
		tong = tong+i;
	}
	printf("tong cac phan tu le cua %d:%d",n,tong);
}
