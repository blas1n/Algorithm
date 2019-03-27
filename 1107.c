#include <stdio.h>
#include <math.h>

int button[10] = { 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 };

int Max(int lhs, int rhs) {
	return lhs > rhs ? lhs : rhs;
}

int Min(int lhs, int rhs) {
	return lhs < rhs ? lhs : rhs;
}

int CheckChannel(int n) {
	if (n == 0 && !button[n])
		return 0;

	while (n > 0) {
		if (!button[n % 10])
			return 0;

		n /= 10;
	}

	return 1;
}

int FindHighChannel(int n) {
	int limit = n + abs(n - 100);

	for (int i = n; i <= limit; i++) {
		if (CheckChannel(i))
			return i;
	}

	return 1000000;
}

int FindLowChannel(int n) {
	int limit = Max(0, n - abs(n - 100));

	for (int i = n; i >= limit; i--) {
		if (CheckChannel(i))
			return i;
	}

	return 1000000;
}

int main() {
	int n, m, tmp, i, nowChannel = 100, ret = 0;
	scanf("%d %d", &n, &m);

	for (i = 0; i < m; i++) {
		scanf("%d", &tmp);
		button[tmp] = 0;
	}

	int high = FindHighChannel(n);
	int low = FindLowChannel(n);

	if (abs(high - n) < abs(n - low))
		nowChannel = high;

	else
		nowChannel = low;

	if (nowChannel) {
		for (tmp = nowChannel; tmp > 0; tmp /= 10)
			ret++;

		printf("%d\n", Min(ret + abs(n - nowChannel), abs(n - 100)));
	}

	else
		printf("%d\n", n + 1);

	
	return 0;
}