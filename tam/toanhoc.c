#include <stdio.h>
#include "libmymath.h"

int main()
{
	int n,x,a;
	printf("nhap n=");
	scanf("%d",&n);
	//--------------------
	printf("nhap x=");
	scanf("%d",&x);
	//-----------------------
	printf("nhap a =");
	scanf("%d",&a);
	//-------------------------
	 gt( n);
	printf("\n");
	 tongchan( n);
	printf("\n");
	 tongle( n);
	printf("\n");
	 luythua(x, a);
	printf("\n");
	return 0;
}
