#include <stdio.h>

int main()
{
    int num1=0,num2=0;
    
    scanf("%d %d",&num1,&num2);
    
    if (num1>num2){
        printf(">\n");
    } else if (num1<num2){
        printf("<\n");
    } else {
        printf("==\n");
    }
    
    
}