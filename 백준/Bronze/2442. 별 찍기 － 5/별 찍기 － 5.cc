#include <iostream>

int main() {
	std::ios::sync_with_stdio(0);
	std::cin.tie(0);

	int N;
	std::cin >> N;

	for (int i = 1; i <= N; i++) {
		//공백 찍는 for문 1개
		for (int j = 1; j <= N - i; j++) {
			std::cout << ' ';
		}
		//별 찍는 for문 1개
		for (int j = 1; j <= 2 * i - 1; j++) {
			std::cout << '*';
		}
		std::cout << '\n';
	}

	return 0;
}