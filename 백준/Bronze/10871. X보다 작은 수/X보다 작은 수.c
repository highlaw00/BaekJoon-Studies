#include <stdio.h>

int main()
{
	int len_list = 0, std_num = 0;
	int num = 0;

	scanf("%d %d", &len_list, &std_num);

	for (int i = 0; i < len_list; i++) {
		scanf("%d", &num);
		if (num < std_num) {
			printf("%d ", num);
		}
	}
	printf("\n");
}