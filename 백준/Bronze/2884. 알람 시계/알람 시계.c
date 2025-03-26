	#include <stdio.h>
	
	int main(){
		
		int hour , minute ;
		
		scanf("%d %d" , &hour , &minute);
		if (hour == 0)
				hour += 24;
				
		if (minute < 45){
			minute += 60 ;
			hour -= 1 ;
			}
		
		minute -= 45;
		if (hour == 24)
			hour = 0 ;
		printf("%d %d",hour , minute);
		
		return 0;
	}