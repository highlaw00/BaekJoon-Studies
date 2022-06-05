#include <iostream>

void ascend_the_list(int* array, int len) {
	int current_solution;
	int temp_index;
	int temp_value;

	//새 배열을 선언하지 않고 존재하는 배열 내에서 swap을 해주는게 필요하다. 
	//메모리를 절약하고 시간 복잡도를 낮추기 위해.
	//swap을 언제하느냐? current_solution이 자기 보다 작은 원소를 만날 때마다 swap을 하게 되면
	//내림차순 배열에선 시간 차원과 계산 차원에선 효율적이지 않을 것입니다.
	//허나 이 부분에 대해선 아직 기법을 모르기 때문에 아는대로 풀어보겠음.

	for (int i = 0; i < len; i += 1) {
		current_solution = array[i];
		for (int j = i + 1; j < len; j += 1) {
			if (current_solution > array[j]) {
				current_solution = array[j];
				temp_index = j;
			}
		}

		if (current_solution != array[i]) {
			//최적해가 변경 되었다면, swap을 해준다.
			temp_value = array[i];
			array[i] = array[temp_index];
			array[temp_index] = temp_value;
		}
	}

}

int sum_of_times(int* array, int len) {
	int result = 0;

	for (int i = 0; i < len; i += 1) {
		for (int j = 0; j <= i; j += 1) {
			result += array[j];
		}
	}

	return result;
}

int main() {
	int total_number = 0;
	std::cin >> total_number;

	int* arr = new int[total_number];

	for (int i = 0; i < total_number; i += 1) {
		std::cin >> arr[i];
	}

	ascend_the_list(arr, total_number);

	std::cout << sum_of_times(arr, total_number);

	delete[] arr;

	return 0;
}