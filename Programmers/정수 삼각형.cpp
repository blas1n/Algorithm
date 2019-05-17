#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int getAnswer(const vector<vector<int>>& triangle, int x, int y) {
	static int cache[500][500] = { 0, };

	if (y == triangle.size() - 1)
		return triangle[y][x];

	if (cache[y][x]) return cache[y][x];

	cache[y][x] = triangle[y][x] + max(getAnswer(triangle, x, y + 1), getAnswer(triangle, x + 1, y + 1));
    return cache[y][x];
}

int solution(vector<vector<int>> triangle) {
    return getAnswer(triangle, 0, 0);
}