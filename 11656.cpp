#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	string word;
	cin >> word;

	vector<string> answers;

	for (int i = word.length() - 1; i >= 0; i--)
		answers.push_back(word.substr(i, word.length() - i));

	sort(answers.begin(), answers.end());

	for (auto ans : answers)
		cout << ans << endl;

	return 0;
}