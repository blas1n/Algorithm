#include <stdio.h>

int n;

void PrintStar(int i) {
	int j;

	for (j = 0; j < n - i; j++)
		putchar(' ');

	for (j = 0; j < i * 2 - 1; j++)
		putchar('*');

	putchar('\n');
}

int main() {
	int i;
	scanf("%d", &n);

	for (i = n; i > 0; i--)
		PrintStar(i);

	for (i = 2; i <= n; i++) {
		PrintStar(i);
	}

	return 0;
}