#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	int count;
	int num1;
	int num2;

	scanf("%d", &count);

	for (int i = 0; i < count; i++)
	{
		scanf("%d %d", &num1, &num2);

		printf("Case #%d: %d\n", i+1, num1 + num2);

	}

	return 0;
}