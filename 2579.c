#include <stdio.h>

int stairs[301];
int cache[301][2];

int Max(int lhs, int rhs) {
	return (lhs > rhs) ? lhs : rhs;
}

int Solution(int n) {
	cache[n][0] = cache[n][1] = stairs[n];

	cache[n - 1][0] = stairs[n - 1] + stairs[n];
	cache[n - 1][1] = 0;

	for (int i = n - 2; i > 0; i--) {
		cache[i][0] = Max(cache[i + 1][1], cache[i + 2][0]) + stairs[i];
		cache[i][1] = cache[i + 2][0] + stairs[i];
	}

	return Max(cache[1][0], cache[2][0]);
}

int main() {
	int n;
	scanf("%d", &n);

	for (int i = 0; i < n; i++)
		scanf("%d", &stairs[i + 1]);

	printf("%d\n", Solution(n));
	return 0;
}