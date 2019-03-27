#include <stdio.h>

void PrintStar(int i) {
	for (int j = 0; j < i; j++)
		putchar('*');

	putchar('\n');
}

int main() {
	int n, i;
	scanf("%d", &n);

	for (i = 1; i <= n; i++)
		PrintStar(i);

	for (i = n - 1; i > 0; i--) {
		PrintStar(i);
	}

	return 0;
}