#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int mini(int* num, int count)
{
	int minimum = *num;
	for (int i = 0; i < count; i++) {
		if (*(num + i) < minimum) {
			minimum = *(num + i);
		}
	}
	return minimum;
}

int maxi(int* num, int count)
{
	int maximum = *num;
	for (int i = 0; i < count; i++)
	{
		if (*(num + i) > maximum) {
			maximum = *(num + i);
		}
	}

	return maximum;
}


int main()
{
	int count;
	int* numarr;
	int temp=0;

	scanf("%d", &count);

	numarr = (int*)malloc(sizeof(int) * count);

	for (int i = 0; i < count;i++) {
		scanf("%d", &temp);
		*(numarr+i) = temp;
	}

	printf("%d %d\n", mini(numarr, count), maxi(numarr, count));

	free(numarr);

	return 0;

}