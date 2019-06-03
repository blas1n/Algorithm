#include <string>
#include <vector>
#include <queue>

using namespace std;

int bridge_weight;

queue<int> wait_truck;
queue<int> cross_truck;

int* delays;
int first, last;

void enter() {
	bridge_weight -= wait_truck.front();
	cross_truck.push(wait_truck.front());
	wait_truck.pop();
	last++;
}

void exit() {
	bridge_weight += cross_truck.front();
	cross_truck.pop();
	first++;
}

int solution(int bridge_length, int weight, vector<int> truck_weights) {
	bridge_weight = weight;
	delays = new int[truck_weights.size()];
	fill(delays, delays + truck_weights.size(), bridge_length);

	for (const auto weight : truck_weights)
		wait_truck.push(weight);

	int answer = 0;

	while (!wait_truck.empty() || !cross_truck.empty()) {
		for (int i = first; i < last; i++)
			if (--delays[i] == 0) exit();
		answer++;

		if (wait_truck.front() > bridge_weight)
			continue;

		if (!wait_truck.empty())
			enter();
	}

	return answer;
}