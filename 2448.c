#include <stdio.h>
#include <stdlib.h>
#include <memory.h>

char** star;

void Solve(int x, int y, int n) {
	if (n == 3) {
		star[y][x] = '*';
		star[y + 1][x - 1] = '*';
		star[y + 1][x + 1] = '*';
		star[y + 2][x - 2] = '*';
		star[y + 2][x - 1] = '*';
		star[y + 2][x] = '*';
		star[y + 2][x + 1] = '*';
		star[y + 2][x + 2] = '*';

		return;
	}

	int div = n / 2;

	Solve(x, y, div);
	Solve(x - div, y + div, div);
	Solve(x + div, y + div, div);
}

int main() {
	int n, i, j;
	scanf("%d", &n);

	star = malloc(n * sizeof(char*));

	for (i = 0; i < n; i++) {
		star[i] = malloc(n * 2 * sizeof(char));
		
		for (j = 0; j < n * 2; j++)
			star[i][j] = ' ';
	}

	Solve(n - 1, 0, n);

	for (i = 0; i < n; i++) {
		for (j = 0; j < n * 2; j++) {
			putchar(star[i][j]);
		}

		putchar('\n');
	}


	return 0;
}