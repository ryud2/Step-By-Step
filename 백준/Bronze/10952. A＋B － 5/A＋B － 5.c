#include <stdio.h>

int main(){
	
	int A, B;
	while(scanf("%d %d" , &A , &B) , A+B != 0){
		printf("%d\n", A+B);
	}
	return 0;
}