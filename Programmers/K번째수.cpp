#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
	vector<int> answer;
	vector<int> subVector;

	for (const auto& command : commands) {
		subVector.clear();

		for (int i = command[0] - 1; i < command[1]; i++)
			subVector.push_back(array[i]);

		sort(subVector.begin(), subVector.end());
		answer.push_back(subVector[command[2] - 1]);
	}

	return answer;
}