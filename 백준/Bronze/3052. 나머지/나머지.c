#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	int numarr[10] = { 0, }; //나머지를 저장하는 배열
	int cnt_num = 0;

	for (int i = 0; i < 10; i++) {
		scanf("%d", &numarr[i]);
		numarr[i] = numarr[i] % 42; //숫자를 입력 받은 뒤 배열에 42로 나눈 나머지를 저장	
	}
	for (int i = 0; i < 10; i++) {
		for (int j = 0; j < 10; j++) {
			if (i >= j) {
				if (i == 9 && j == 9) {
					cnt_num+=1;
				}
				continue;
			}
			else if (numarr[i] == numarr[j]) {
				break;
			}
			else if (numarr[i] != numarr[j]) {
				if (j == 9) {
					cnt_num += 1;
				}
				else {
					continue;
				}
			}
		}
	}

	printf("%d\n", cnt_num);
}