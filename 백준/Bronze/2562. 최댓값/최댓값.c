#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	int numarr[9];
	int count = 1;

	for (int i = 0; i < 9; i++) {
		scanf("%d", &numarr[i]);
	}

	int max = *numarr;

	for (int i = 0; i < 9; i++) {
		if (*(numarr + i) > max) {
			max = *(numarr + i);
			count = i + 1;
		}
	}

	printf("%d \n%d", max, count);

	return 0;
}