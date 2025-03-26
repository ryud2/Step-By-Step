#include <stdio.h>

int main(){
	
	
	
	int a , b , c , money ;
	scanf("%d %d %d" , &a ,&b , &c);
	if (a == b && b == c)
		money = 10000+ a*1000;
		
	else if (a == b || c == a)
		money = 1000 + a*100 ;
		
	else if (b == c)
		money = 1000 + b*100 ;	
	
	else {
		if (b > a) 
			a = b ;
		if (c > a && c > b)
			a = c ;
		money = 100*a ;
		
	}
	
	printf("%d" , money) ;
	
	return 0;
}