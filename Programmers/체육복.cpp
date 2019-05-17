#include <string>
#include <vector>

using namespace std;

int cache[30];

int solution(int n, vector<int> losts, vector<int> reserves) {
	for (int i = 0; i < n; i++)
		cache[i] = 1;

	for (int lost : losts)
		cache[lost - 1]--;

	for (int reserve : reserves)
		cache[reserve - 1]++;
	
	for (int i = 0; i < n; i++) {
		if (cache[i] != 0) continue;

		if (i > 0 && cache[i - 1] == 2) {
			cache[i - 1]--;
			cache[i]++;
			continue;
		}

		if (i + 1 < n && cache[i + 1] == 2) {
			cache[i + 1]--; 
			cache[i]++;
			continue;
		}
	}

	int answer = 0;

	for (int i = 0; i < n; i++) {
		if (cache[i] != 0)
			answer++;
	}

	return answer;
}