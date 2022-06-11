#include <stdio.h>

int main()
{
	int num = 0;

	scanf("%d", &num);

	//제한 범위에 따른 오류 출력
	if (num > 100 || num < 1) {
		printf("Invalid number entered.\n");
		return 0;
	}

	for (int i = 1;i <= num;i++){
		for (int j = 1;j <= num;j++) {
			if (j <= num - i) {
				printf(" ");
			}
			else {
				printf("*");
			}
		}
		printf("\n");
		}
	return 0;
}
