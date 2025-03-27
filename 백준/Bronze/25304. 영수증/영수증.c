#include <stdio.h>

int main(){
	
	int X , N , a , b ;
	
	scanf("%d",&X);
	scanf("%d",&N);
	
	for (int i = 0 ; i < N ; i++){
		a == 0 ;
		b == 0 ;		
		scanf("%d %d ",&a , &b);
		X -= a*b ;
	}
	if (X == 0)
		printf("Yes");
	else
		printf("No");
	
	return 0;
}