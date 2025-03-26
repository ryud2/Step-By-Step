#include <stdio.h>

int main(){
	
	int A,B ,B1 ,B2 ,B3;
	scanf("%d%d",&A,&B);
	B1 = B%10 ;
	B2 = (B/10)%10 ;
	B3 = (B/100)%10 ;
	printf("%d\n%d\n%d\n%d",A*B1,A*B2,A*B3,A*B) ;
	return 0 ;
}