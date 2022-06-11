#include <iostream>

int main() {
	std::ios::sync_with_stdio(0);
	std::cin.tie(0);

	int N;
	std::cin >> N;

	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			if (i > j) std::cout << ' ';
			else std::cout << '*';
		}
		std::cout << '\n';
	}
}