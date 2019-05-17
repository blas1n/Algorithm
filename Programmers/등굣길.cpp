#include <string>
#include <vector>

using namespace std;

int cache[101][101];

int get(int x, int y) {
	if (cache[y][x] == -1)
		return 0;

	return cache[y][x];
}

int solution(int m, int n, vector<vector<int>> puddles) {
	cache[1][1] = 1;

	for (const auto& puddle : puddles) {
		cache[puddle[1]][puddle[0]] = -1;
	}

	for (int y = 1; y <= n; y++) {
		for (int x = 1; x <= m; x++) {
			if (!cache[y][x])
				cache[y][x] = (get(x, y - 1) + get(x - 1, y)) % 1000000007;
		}
	}

	return cache[n][m];
}