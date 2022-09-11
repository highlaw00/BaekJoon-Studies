#include <stdio.h>

int main()
{
	int num_case = 0, num1 = 0, num2 = 0;

	scanf("%d", &num_case);

	for (int i = 1;i <= num_case;i++) {
		scanf("%d %d", &num1, &num2);

		//제한 범위에 따른 오류 출력
		if (num1 >= 10 || num2 >= 10 || num1 <= 0 || num2 <= 0) {
			printf("Invalid number entered.\n");
			return 0;
		}

		printf("Case #%d: %d + %d = %d\n", i, num1, num2, num1 + num2);
	}

	return 0;
}
