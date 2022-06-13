#include <iostream>
#include <vector>

int main() {
	std::ios::sync_with_stdio(0);
	std::cin.tie(0);

	int N, target_num, tmp;
	int cnt = 0;
	std::cin >> N;
	std::vector<int> v1;

	for (int i = 0; i < N; i++) {
		std::cin >> tmp;
		v1.push_back(tmp);
	}

	std::cin >> target_num;

	for (int i = 0; i < N; i++) {
		if (v1[i] == target_num) cnt++;
	}

	std::cout << cnt << '\n';

	return 0;
}
