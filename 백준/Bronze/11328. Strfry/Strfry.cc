#include <iostream>
#include <string>

bool is_strfry_possible(std::string &s1, std::string &s2) {
	int dict1[26] = {};
	int dict2[26] = {};

	int idx;
	if (s1.length() != s2.length()) return false;

	for (int i = 0; i < s1.length(); i++) {
		// s1,s2의 구성 정보를 dict1,dict2에 담습니다.
		idx = s1[i] - 'a';
		dict1[idx]++;
		idx = s2[i] - 'a';
		dict2[idx]++;
	}

	for (int i = 0; i < 26; i++) {
		// dict1과 dict2의 구성 정보를 비교합니다.
		if (dict1[i] != dict2[i]) return false;
	}

	return true;
}

int main() {
	std::ios::sync_with_stdio(0);
	std::cin.tie(0);

	int test_case;
	std::string str1, str2;

	std::cin >> test_case;

	for (int i = 0; i < test_case; i++) {
		std::cin >> str1 >> str2;

		if (is_strfry_possible(str1, str2)) std::cout << "Possible\n";
		else std::cout << "Impossible\n";

		str1.clear();
		str2.clear();
	}

	return 0;
}