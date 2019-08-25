#include <vector>

using namespace std;

inline int GetRed(int x, int y)
{
	return (x - 2) * (y - 2);
}

inline int GetBrown(int x, int y)
{
	return (x - 1) * 2 + (y - 1) * 2;
}

vector<int> solution(int brown, int red) {
	for (int x = 3; ; x++)
		for (int y = 3; y <= x; y++)
			if (GetRed(x, y) == red && GetBrown(x, y) == brown)
				return vector<int>{x, y};
}