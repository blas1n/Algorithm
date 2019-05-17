#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> citations) {
	sort(citations.begin(), citations.end());

	for (int i = 0; i < citations.size(); i++) {
		if (citations.size() - i <= citations[i]) {
            return citations.size() - i;
        }
	}

	return 0;
}