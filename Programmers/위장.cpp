#include <string>
#include <vector>
#include <map>

using namespace std;

map<string, int> clothMap;

void initMap(const vector<vector<string>>& clothes) {
	for (const auto& cloth : clothes) {
		if (clothMap.find(cloth[1]) != clothMap.end())
			clothMap[cloth[1]]++;

		else
			clothMap.insert(make_pair(cloth[1], 1));
	}
}

int solution(vector<vector<string>> clothes) {
	initMap(clothes);

	int ans = 1;

	for (const auto& cloth : clothMap)
		ans *= (cloth.second + 1);

	return ans - 1;
}