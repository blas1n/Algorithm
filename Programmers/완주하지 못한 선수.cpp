#include <string>
#include <vector>
#include <queue>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
	priority_queue<string> participantHeap;
	priority_queue<string> completionHeap;

	for (auto p : participant)
		participantHeap.push(p);

	for (auto c : completion)
		completionHeap.push(c);

	while (!completionHeap.empty()) {
		if (participantHeap.top() != completionHeap.top())
			return participantHeap.top();

		participantHeap.pop();
		completionHeap.pop();
	}

	return participantHeap.top();
}