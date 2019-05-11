#include <iostream>
#include <string>

using namespace std;

int Solution(const string& str) {
	int ret = 0;

	for (int i = 0; i < str.length(); i++) {
		if (str[i] == 'c') {
			if (str[i + 1] == '=' || str[i + 1] == '-')
				i++;
		}

		else if (str[i] == 'd') {
			if (str[i + 1] == 'z' && str[i + 2] == '=')
				i += 2;

			else if (str[i + 1] == '-')
				i++;
		}

		else if (str[i] == 'l') {
			if (str[i + 1] == 'j')
				i++;
		}

		else if (str[i] == 'n') {
			if (str[i + 1] == 'j')
				i++;
		}

		else if (str[i] == 's') {
			if (str[i + 1] == '=')
				i++;
		}

		else if (str[i] == 'z') {
			if (str[i + 1] == '=')
				i++;
		}

		ret++;
	}

	return ret;
}

int main() {
	string str;
	cin >> str;

	cout << Solution(str);
	return 0;
}