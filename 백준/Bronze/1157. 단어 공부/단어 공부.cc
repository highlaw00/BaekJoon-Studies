#include <iostream>
using namespace std;

int main() {
	char* word = new char[1000000];
	int* alphabet_cnt = new int[26]{ 0, };

	cin >> word;

	for (int i = 0; word[i] != NULL; i++) {
		if (word[i] >= 'A' && word[i] <= 'Z') {
			alphabet_cnt[word[i] - 'A']++;
		}
		else if (word[i] >= 'a' && word[i] <= 'z') {
			alphabet_cnt[word[i] - 'a']++;
		}
	}

	int max_val = alphabet_cnt[0];
	int max_index = 0;
	bool isitoverlap = false;

	for (int i = 0; i < 26; i++) {
		if (max_val <= alphabet_cnt[i]) {
			max_val = alphabet_cnt[i];
			max_index = i;
		}
	}

	for (int i = 0; i < 52; i++) {
		if (max_val == alphabet_cnt[i] && max_index != i) {
			isitoverlap = true;
		}
	}

	if (isitoverlap) {
		cout << '?' << endl;
		return 0;
	}
	else {
		cout << (char)(max_index + 'A') << endl;
	}

	return 0;
}