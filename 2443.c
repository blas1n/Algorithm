#include <stdio.h>

int main() {
	int n, i, j;
	scanf("%d", &n);

	for (i = 1; i <= n; i++) {
		for (j = 0; j < i - 1; j++)
			putchar(' ');
		for (j = 0; j < (n * 2) - (i * 2) + 1; j++)
			putchar('*');

		putchar('\n');
	}

	return 0;
}