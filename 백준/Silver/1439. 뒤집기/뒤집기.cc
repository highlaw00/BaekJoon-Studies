#include <iostream>
#include <string>

int calculate_switch_number(std::string str) {
	int zero_counter = 0;
	int one_counter = 0;
	int string_len = str.length();
	char prev_char = str[0];
	char curr_char = str[0];

	if (curr_char == '0') zero_counter += 1;
	//문자열의 첫 문자가 0일 경우 0 뭉탱이가 1개 이상이란 뜻이니 0 counter를 + 1 해준다.
	else one_counter += 1;
	//문자열의 첫 문자가 1일 경우 1 뭉탱이가 1개 이상이란 뜻이니 1 counter를 + 1 해준다.

	for (int i = 0; i < string_len; i += 1) {
		curr_char = str[i];

		if (curr_char == prev_char) {
			//이전 문자와 현재 문자가 동일하다면 다음 반복문으로 넘어간다.
		}
		else if (curr_char != prev_char) {
			//이전 문자와 현재 문자가 다를 경우
			if (curr_char == '0') {
				//현재 문자가 0, 이전 문자가 1 -> 0 counter를 + 1 해준다.
				zero_counter += 1;
			}
			else one_counter += 1;
				//현재 문자가 1, 이전 문자가 0 -> 1 counter를 + 1 해준다.
		}

		prev_char = curr_char;
	}

	int result;
	result = (zero_counter >= one_counter) ? one_counter : zero_counter;
	//둘 중 적은것을 return 한다.

	return result;
}

int main() {
	std::string sentence;
	getline(std::cin, sentence);

	std::cout << calculate_switch_number(sentence) << std::endl;

	return 0;
}