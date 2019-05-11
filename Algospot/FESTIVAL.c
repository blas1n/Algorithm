#include <stdio.h>

#define MIN(lhs, rhs) (((lhs) < (rhs)) ? (lhs) : (rhs))

int board[1001];
double cache[1001];

double getMinAverage(int n, int l) {
	double minAverage = 100.0;

	for (int i = 0; i <= n - l; i++) {
		double sum = 0.0;
		for (int j = i; j < i + l - 1; j++) {
			sum += board[j];
		}

		cache[i] = 100.0;
		for (int j = i + l - 1; j < n; j++) {
			sum += board[j];
			double partialAverage = sum / (j - i + 1);
			cache[i] = MIN(cache[i], partialAverage);
		}
		minAverage = MIN(minAverage, cache[i]);
	}

	return minAverage;
}

int main() {
	int c;
	scanf("%d\n", &c);

	while (c--) {
		int n, l;
		scanf("%d %d", &n, &l);

		for (int j = 0; j < n; j++) {
			scanf("%d", &board[j]);
		}

		printf("%.12f\n", getMinAverage(n, l));
	}

	return 0;
}