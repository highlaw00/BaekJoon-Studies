#include <iostream>

/* 
1. Ai 배열들의 원소와 만드려는 가치의 합인 K를 대소비교 하여 그 중 가장 큰 값(그러나 K보다는 작아야 함)
2. K를 1번에서 선택한 원소와 나눠준다.
3. 그리고 그 몫을 기록한다.
4. K를 1번에서 선택한 원소로 나눠준 나머지를 Kn이라고 지칭. 그리고 이 작업은 Kn이 0이 될 때까지 반복한다.
*/

int calculate(int* arr, int amount_of_types, int target_value) {
	int amount_of_coins = 0;
	int biggest_coin = 0;
	int remain_value = target_value;

	while(remain_value > 0) {
		//Kn이 0보다 클 때
		biggest_coin = arr[0];
		for (int i = 0; i < amount_of_types; i += 1) {
			//Greedy Algorithm을 이용해 동전 배열 중 최적해를 구한다.
			if (biggest_coin <= arr[i] && arr[i] <= remain_value) {
				//새로운 최적해를 찾을 경우.
				biggest_coin = arr[i];
			}
			else break;
		}

		amount_of_coins += remain_value / biggest_coin;
		remain_value = remain_value % biggest_coin;
	}

	return amount_of_coins;
}


int main() {
	int types_of_coin;
	int target;
	int result;

	std::cin >> types_of_coin >> target;

	int* coin_array = new int[types_of_coin];

	for (int i = 0; i < types_of_coin; i += 1) {
		std::cin >> coin_array[i];
	}

	result = calculate(coin_array, types_of_coin, target);

	std::cout << result << std::endl;

	return 0;
}