#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> budgets, int M) {
	auto minVal = 0;
	auto maxVal = *max_element(budgets.cbegin(), budgets.cend());

	auto val = 0;
	for (val = (maxVal + minVal) / 2; minVal <= maxVal; val = (maxVal + minVal) / 2) {
		auto sum = 0;
		for (auto budget : budgets)
			sum += min(budget, val);

		if (sum > M)
			maxVal = val - 1;
		else if (sum < M)
			minVal = val + 1;
		else
			break;
	}

	return val;
}