#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> prices) {
	vector<int> answer(prices.size());

	for (int i = prices.size() - 1; i >= 0; i--) {
		for (int j = i + 1; j < prices.size(); j++) {
			answer[i]++;

			if (prices[i] > prices[j])
				break;
		}
	}

	return answer;
}