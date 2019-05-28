#include <iostream>
#include <queue>

using namespace std;

priority_queue<long long> heap;

int main() {
	int n;
	cin >> n;

	long long buf;

	for (int i = 0; i < n; i++) {
		cin >> buf;
		heap.push(buf);
	}

	long long max, maxCount, now, nowCount;
	max = maxCount = 0;

	while (maxCount <= heap.size()) {
		nowCount = 0;
		now = heap.top();
		
		while (!heap.empty() && heap.top() == now) {
			heap.pop();
			nowCount++;
		}

		if (maxCount <= nowCount) {
			max = now;
			maxCount = nowCount;
		}
	}
	
	cout << max << endl;
	return 0;
}