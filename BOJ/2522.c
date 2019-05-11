#include <stdio.h>

int n;

void PrintStar(int i) {
	int j;

	for (j = 0; j < n - i; j++)
		putchar(' ');

	for (j = 0; j < i; j++)
		putchar('*');

	putchar('\n');
}

int main() {
	int i;
	scanf("%d", &n);

	for (i = 1; i <= n; i++)
		PrintStar(i);

	for (i = n - 1; i > 0; i--) {
		PrintStar(i);
	}

	return 0;
}