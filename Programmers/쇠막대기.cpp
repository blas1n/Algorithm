#include <string>
#include <vector>

using namespace std;

int solution(string arrangement) {
    int answer = 0;
	int stickNum = 0;

	for (int i = 0; i < arrangement.length(); i++) {
		if (arrangement[i] == '(') {
			if (arrangement[i + 1] == ')') {
				answer += stickNum;
				i++;
				continue;
			}

			stickNum++;
		}

		else {
			stickNum--;
			answer++;
		}
	}

	return answer;
}