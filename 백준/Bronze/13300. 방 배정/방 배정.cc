#include <iostream>

int main() {
	std::ios::sync_with_stdio(0);
	std::cin.tie(0);

	int total, capa, sex, grade;
	int room_cnt = 0;
	int** room = new int* [2];
	for (int i = 0; i < 2; i++) room[i] = new int[6];

	for (int i = 0; i < 2; i++) {
		for (int j = 0; j < 6; j++) {
			room[i][j] = 0;
		}
	}

	std::cin >> total >> capa;

	for (int i = 0; i < total; i++) {
		std::cin >> sex >> grade;
		room[sex][grade - 1]++;
	}

	for (int i = 0; i < 2; i++) {
		for (int j = 0; j < 6; j++) {
			room_cnt += room[i][j] / capa;
			if (room[i][j] % capa != 0) {
				room_cnt++;
			}
		}
	}

	/*
		for (int i = 0; i < 2; i++) {
			for (int j = 0; j < 6; j++) {
				std::cout << room[i][j] << ' ';
			}
			std::cout << '\n';
		}
	*/

	std::cout << room_cnt;

	return 0;
}