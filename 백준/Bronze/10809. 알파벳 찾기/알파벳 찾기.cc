#include <stdio.h>

int main()
{
	char string[101];
	int count = 0;

	scanf("%s", string);

	for (char i = 'a'; i <= 'z'; i++) {
		count = 0;
		for (int j = 0; string[j]!=NULL; j++) {
			if (i == string[j]) {
				printf("%d ", j);
				count = 1;
				break;
			}

		}
		if (count == 0) {
			printf("-1 ");
		}
	}
	return 0;
}