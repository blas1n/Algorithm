#include <stdio.h>

int main() {
	int n, i, j;
	scanf("%d", &n);

	for (i = 1; i <= n; i++) {
		for (j = 0; j < n - i; j++)
			putchar(' ');
		for (j = 0; j < i * 2 - 1; j++)
			putchar('*');

		putchar('\n');
	}

	for (i = n - 1; i >= 1; i--) {
		for (j = 0; j < n - i; j++)
			putchar(' ');
		for (j = 0; j < i * 2 - 1; j++)
			putchar('*');

		putchar('\n');
	}

	return 0;
}