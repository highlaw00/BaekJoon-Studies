#include <iostream>

int main() {
	std::ios::sync_with_stdio(0);
	std::cin.tie(0);

	int N;
	std::cin >> N;

	for (int i = N; i > 0; i--) {
		// 별 출력을 2*k -1 번 한다.
		// 공백 출력은? N과 i의 차이 만큼 출력해주면 됨. 
		for (int j = 1; j <= N - i; j++) std::cout << ' ';
		for (int j = 1; j <= 2 * i - 1; j++) std::cout << '*';

		std::cout << '\n';
	}

	return 0;
}