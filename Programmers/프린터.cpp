#include <vector>
#include <queue>

using namespace std;

int solution(vector<int> priorities, int location) {
	queue<int> prints;
	priority_queue<int> orders;
	
	for (auto prioritie : priorities) {
		prints.push(prioritie);
		orders.push(prioritie);
	}

	int answer = 1;

	while (true) {
		if (prints.front() == orders.top()) {
			prints.pop();
			orders.pop();

			if (location == 0)
				break;

			answer++;
		}

		else {
			prints.push(prints.front());
			prints.pop();
		}

		if (--location < 0)
			location = prints.size() - 1;
	}

	return answer;
}