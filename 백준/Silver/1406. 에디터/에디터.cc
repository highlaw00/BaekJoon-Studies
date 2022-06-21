#include <iostream>
#include <string>
#include <list>

int main() {
	std::ios::sync_with_stdio(0);
	std::cin.tie(0);

	std::string str;
	std::list<char> sentence;

	std::cin >> str;
	for (int i = 0; i < str.length(); i++) sentence.push_back(str[i]);
	std::list<char>::iterator it = sentence.end();

	int n;
	char com;
	std::cin >> n;
	while (n--) {
		std::cin >> com;
		if (com == 'P') {
			char add;
			std::cin >> add;
			sentence.insert(it, add);
		}
		else if (com == 'L') {
			if (it != sentence.begin()) {
				it--;
			}
		}
		else if (com == 'D') {
			if (it != sentence.end()) {
				it++;
			}
		}
		else {
			// 'B' 의 기능
			if (it != sentence.begin()) {
				it--;
				it = sentence.erase(it);
			}
		}
	}

	for (it = sentence.begin(); it != sentence.end(); it++) {
		std::cout << *it;
	}

	return 0;
}