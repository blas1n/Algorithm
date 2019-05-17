#include <vector>
#include <queue>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
	queue<int> durations;

	for (int i = 0; i < progresses.size(); i++) {
		int left = (100 - progresses[i]);
		int duration = left / speeds[i];

		if (left % speeds[i]) duration++;

		durations.push(duration);
	}

	vector<int> answer;

	while (!durations.empty()) {
		int ans = 1;
		int top = durations.front();

		while (true) {
			durations.pop();

			if (durations.empty() || top < durations.front())
				break;

			ans++;
		}

		answer.push_back(ans);
	}

	return answer;
}