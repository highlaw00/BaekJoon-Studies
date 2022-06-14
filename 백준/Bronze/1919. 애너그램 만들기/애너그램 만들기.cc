#include <iostream>
#include <string>

int main() {
	std::ios::sync_with_stdio(0);
	std::cin.tie(0);
	
	std::string str1, str2;
	int arr[26] = {};
	int cnt = 0;
	char tmp;

	std::getline(std::cin, str1);
	std::getline(std::cin, str2);

	for (int i = 0; i < str1.length(); i++) {
		tmp = str1[i] - 'a';
		arr[tmp]++;
	}

	for (int i = 0; i < str2.length(); i++) {
		tmp = str2[i] - 'a';
		arr[tmp]--;
	}

	for (int i = 0; i < 26; i++) {
		if (arr[i] != 0) cnt += std::abs(arr[i]);
	}

	std::cout << cnt;

	return 0;
}