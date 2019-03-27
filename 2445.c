#include <stdio.h>

void PrintStar(int n, int i) {
	int j;

	for (j = 0; j < i; j++)
		putchar('*');

	for (j = 0; j < (n * 2) - (i * 2); j++)
		putchar(' ');

	for (j = 0; j < i; j++)
		putchar('*');

	putchar('\n');
}

int main() {
	int n, i;
	scanf("%d", &n);

	for (i = 1; i <= n; i++)
		PrintStar(n, i);

	for (i = n - 1; i >= 1; i--) {
		PrintStar(n, i);
	}

	return 0;
}