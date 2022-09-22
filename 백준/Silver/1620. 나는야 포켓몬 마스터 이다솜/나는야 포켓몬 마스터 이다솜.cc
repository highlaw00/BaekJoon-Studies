#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstring>
#include <cmath>
using namespace std;


class Pocketmon {
private:
	char name[21];
	int id;
public:
	Pocketmon() {
	}
	void setName(char* string) {
		strcpy(this->name, string);
	}
	void setId(int id) {
		this->id = id;
	}
	char* getName() {
		return this->name;
	}
	int getId() {
		return this->id;
	}
};

int binarySearch(Pocketmon* arr, int len, char* string) {
	int start = 0;
	int end = len - 1;
	int middle = (start + end) / 2;
	while (1) {
		if (strcmp(arr[middle].getName(), string) == 0) {
			return arr[middle].getId();
		}
		else if (strcmp(arr[middle].getName(), string) > 0) {
			end = middle - 1;
			middle = (start + end) / 2;
		}
		else if (strcmp(arr[middle].getName(), string) < 0) {
			start = middle + 1;
			middle = (start + end) / 2;
		}
	}
}


void swap(Pocketmon* p1, Pocketmon* p2) {
	Pocketmon temp;
	temp = *p1;
	*p1 = *p2;
	*p2 = temp;
}

void quickSort(Pocketmon* arr, int start, int end) {
	int pivot = start;
	int i = start + 1;
	int j = end;
	if (i > j) { return; }
	while (i <= j) {
		//i는 pivot의 뒤에 위치해야한다.
		//따라서 pivot보다 큰 값이 나온다면? swap해줘야한다.
		while (i <= end && strcmp(arr[i].getName(),arr[pivot].getName()) < 0) { i++; }
		//j는 pivot보다 앞에 위치해야한다. (즉, 값이 작아야됨)
		//따라서 pivot보다 작은 값이 나온다면 swap한다.
		while (j > start&& strcmp(arr[j].getName(), arr[pivot].getName()) > 0) { j--; }
		if (i > j) { swap(&arr[j], &arr[pivot]); }
		else { swap(&arr[i], &arr[j]); }
	}
	quickSort(arr, start, j - 1);
	quickSort(arr, j + 1, end);
}

int main() {
	int book_len;
	int quest_amt;
	char temp[21];

	cin >> book_len >> quest_amt;

	Pocketmon* book_by_num = new Pocketmon[book_len];
	Pocketmon* book_by_name = new Pocketmon[book_len];


	for (int i = 0; i < book_len; i++) {
		scanf("%s", temp);
		book_by_num[i].setName(temp);
		book_by_name[i].setName(book_by_num[i].getName());
		book_by_num[i].setId(i + 1);
		book_by_name[i].setId(i + 1);
	}

	int sum = 0;
	int id = 0;

	quickSort(book_by_name, 0, book_len - 1);
	
	for (int i = 0; i < quest_amt; i++) {
		scanf("%s", temp);

		if (temp[0] >= '0' && temp[0] <= '9') { // 숫자인 경우
			sum = atoi(temp);
			printf("%s\n", book_by_num[sum - 1].getName());
		}
		else { // 문자인 경우
			id = binarySearch(book_by_name, book_len, temp);
			printf("%d\n", id);
		}
	}
	
	delete[] book_by_name;
	delete[] book_by_num;

	return 0;
}