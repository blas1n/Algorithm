#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> people, int limit) {
	sort(people.begin(), people.end());

	int pair = 0;
	int light = 0;
	int heavy = people.size() - 1;

	while (light < heavy) {
		if (people[light] + people[heavy] <= limit) {
			light++;
			heavy--;
			pair++;
		}

		else {
			heavy--;
		}
	}

	return people.size() - pair;
}