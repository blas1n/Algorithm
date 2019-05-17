#include <string>
#include <vector>

using namespace std;

int failer[3][10] = {
	{1, 2, 3, 4, 5},
	{2, 1, 2, 3, 2, 4, 2, 5},
	{3, 3, 1, 1, 2, 2, 4, 4, 5, 5}
};

int failerNum[3] = { 5, 8, 10 };

vector<int> solution(vector<int> answers) {
	int failerAnswerNum[3] = { 0, };
	int max = 0;

	for (int i = 0; i < 3; i++) {
		for (int index = 0; index < answers.size(); index++) {
			if (answers[index] == failer[i][index % failerNum[i]])
				failerAnswerNum[i]++;
		}

		max = (failerAnswerNum[i] > max) ? failerAnswerNum[i] : max;
	}

	vector<int> answer;

	for (int i = 0; i < 3; i++) {
		if (failerAnswerNum[i] == max)
			answer.push_back(i + 1);
	}

	return answer;
}