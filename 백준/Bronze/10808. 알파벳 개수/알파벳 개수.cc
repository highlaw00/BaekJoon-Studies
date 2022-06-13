#include <iostream>
#include <string>
#include <vector>

int main() {
	std::string str1;
	std::vector<int> dict(26);
	std::getline(std::cin, str1);
	int idx;

	for (int i = 0; i < str1.length(); i++) {
		idx = str1[i] - 'a';
		dict[idx]++;
	}

	for (int i = 0; i < dict.size(); i++) {
		std::cout << dict[i] << " ";
	}

	std::cout << '\n';

	return 0;
}