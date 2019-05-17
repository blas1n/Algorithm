#include <vector>

using namespace std;

int cache[2000][2000];

vector<int> leftCards;
vector<int> rightCards;

constexpr int max(int lhs, int rhs) {
	return lhs > rhs ? lhs : rhs;
}

int getAnswer(int leftIndex, int rightIndex) {
	int value = 0, right = rightIndex;

	if (leftIndex >= leftCards.size() || rightIndex >= rightCards.size())
		return 0;

	if (cache[leftIndex][rightIndex])
		return cache[leftIndex][rightIndex];

	if (leftCards[leftIndex] > rightCards[rightIndex]) {
		cache[leftIndex][rightIndex] = rightCards[rightIndex];
		right++;

		value = getAnswer(leftIndex, right);
	}

	int left = getAnswer(leftIndex + 1, right);
	int all = getAnswer(leftIndex + 1, right + 1);

	cache[leftIndex][rightIndex] += max(value, max(left, all));
	
	return cache[leftIndex][rightIndex];
}

int solution(vector<int> left, vector<int> right) {
	leftCards = move(left);
	rightCards = move(right);

	return getAnswer(0, 0);
}