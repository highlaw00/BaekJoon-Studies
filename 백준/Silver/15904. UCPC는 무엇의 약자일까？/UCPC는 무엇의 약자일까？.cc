#include <iostream>
#include <string>

bool is_it_UCPC(std::string sentence) {
	char target_sentence[5] = "UCPC";
	int len = sentence.length();
	int counter = 0;
	int last_index = -1;

	for (int i = 0; i < 4; i += 1) {
		for (int j = last_index + 1; j < len; j += 1) {
			if (target_sentence[i] == sentence[j]) {
				counter += 1;
				last_index = j;
				break;
			}
		}
		if (counter == 4) return true;
	}
	return false;
}

int main() {
	std::string input_sentence;
	std::getline(std::cin, input_sentence);

	bool result = is_it_UCPC(input_sentence);

	if (result) {
		std::cout << "I love UCPC" << std::endl;
	}
	else std::cout << "I hate UCPC" << std::endl;

	return 0;
}