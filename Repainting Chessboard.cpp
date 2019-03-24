#include <iostream>
#include <string>

using namespace std;

char board[51][51] = { 0, };

const char blackboard[9][9] = {
	{"BWBWBWBW"},
	{"WBWBWBWB"},
	{"BWBWBWBW"},
	{"WBWBWBWB"},
	{"BWBWBWBW"},
	{"WBWBWBWB"},
	{"BWBWBWBW"},
	{"WBWBWBWB"},
};

const char whiteboard[9][9] = {
	{"WBWBWBWB"},
	{"BWBWBWBW"},
	{"WBWBWBWB"},
	{"BWBWBWBW"},
	{"WBWBWBWB"},
	{"BWBWBWBW"},
	{"WBWBWBWB"},
	{"BWBWBWBW"},
};

int Min(int lhs, int rhs) {
	return lhs < rhs ? lhs : rhs;
}

int CheckBlackboard(int x, int y) {
	int ret = 0;

	for (int i = y; i < y + 8; i++) {
		for (int j = x; j < x + 8; j++) {
			if (board[i][j] != blackboard[i - y][j - x])
				ret++;
		}
	}

	return ret;
}

int CheckWhiteboard(int x, int y) {
	int ret = 0;

	for (int i = y; i < y + 8; i++) {
		for (int j = x; j < x + 8; j++) {
			if (board[i][j] != whiteboard[i - y][j - x])
				ret++;
		}
	}

	return ret;
}

int main() {
	int m, n, result = 64;
	cin >> m >> n;

	for (int i = 0; i < m; i++)
		cin >> board[i];
	
	for (int i = 0; i <= n - 8; i++) {
		for (int j = 0; j <= m - 8; j++) {
			result = Min(result, Min(CheckBlackboard(i, j), CheckWhiteboard(i, j)));
		}
	}

	printf("%d\n", result);
	return 0;
}