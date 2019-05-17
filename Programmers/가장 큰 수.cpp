#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(vector<int> numbers) {
	vector<string> strNum(numbers.size());

	for (int i = 0; i < numbers.size(); i++)
		strNum[i] = to_string(numbers[i]);

	sort(strNum.begin(), strNum.end(), [](const string& lhs, const string& rhs) {
		return (lhs + rhs) > (rhs + lhs);
	});

	if (strNum[0] == "0")
		return "0";

	string answer = "";

	for (const auto& str : strNum)
		answer.append(str);

	return answer;
}