#include <stdio.h>

void gt(int n)
{
	int i, gt = 1;
	for (i = 1;i <= n;i ++)
	{
		gt = gt*i;
	}
	printf("giai thua cua %d:%d",n,gt);

}
