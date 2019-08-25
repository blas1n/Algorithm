#include <string>
#include <vector>
#include <set>

using namespace std;

vector<int> solution(vector<string> operations) {
	multiset<int, greater<int>> queue;
	char command;
	int num;
	
	for (const auto& oper : operations) {
		sscanf(oper.c_str(), "%c %d", &command, &num);

		if (command == 'I')
			queue.insert(num);
		else if (!queue.empty()) {
			if (num == 1)
				queue.erase(queue.begin());
			else
				queue.erase(--queue.end());
		}
	}
	
	if (queue.empty())
		return  { 0, 0 };
	return { *queue.begin(), *--queue.end() };
}