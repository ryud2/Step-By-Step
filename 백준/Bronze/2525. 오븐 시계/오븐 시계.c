	#include <stdio.h>
	
	int main(){
		
		int hour , minute , take ;
		
		scanf("%d%d%d",&hour , &minute , &take);
		
		minute += take;
		while (minute>=60){
			minute -= 60;
			hour += 1;
		}
		if (hour >= 24)
			hour -= 24 ;
			
		printf("%d %d",hour, minute);
		return 0;
	}