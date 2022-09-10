#include <stdio.h>

int main()
{
    char* hello="Hello World!";
    
    for (int i=0; hello[i]!='\0';i++){
        printf("%c",hello[i]);
    }
}