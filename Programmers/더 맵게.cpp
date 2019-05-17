#include <vector>
#include <queue>

using namespace std;

int solution(vector<int> scoville, int K) {
	priority_queue<int, vector<int>, greater<int>> foods;

	for (auto s : scoville)
		foods.push(s);

	int answer = 0;

	while (true) {
		if (foods.top() >= K)
			return answer;

		if (foods.size() < 2)
			break;

		int first = foods.top();
		foods.pop();
		int second = foods.top();
		foods.pop();

		foods.push(first + (second * 2));
		answer++;
	}
	
	return -1;
}