#include <stdio.h>

#define MIN(lhs, rhs) ((lhs < rhs) ? lhs : rhs)

int main() {
	int n;
	scanf("%d", &n);

	int count2 = 0, count5 = 0;

	for (int i = 2; i <= n; i++) {
		if ((i % 2) && (i % 5)) continue;

		int elem = i;

		while (elem % 2 == 0) {
			count2++;
			elem /= 2;
		}

		while (elem % 5 == 0) {
			count5++;
			elem /= 5;
		}
	}

	printf("%d\n", MIN(count2, count5));
	return 0;
}