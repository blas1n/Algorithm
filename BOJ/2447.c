#include <stdio.h>
#include <stdlib.h>
#include <memory.h>

char** star;

void Solve(int x, int y, int n) {
	if (n == 1) {
		star[y][x] = '*';
		return;
	}	

	int div = n / 3;

	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 3; j++) {
			if (i != 1 || j != 1)
				Solve(x + (j * div), y + (i * div), div);
		}
	}
}

int main() {
	int n, i, j;
	scanf("%d", &n);

	star = malloc(n * sizeof(char*));

	for (i = 0; i < n; i++) {
		star[i] = malloc(n * sizeof(char));
		
		for (j = 0; j < n; j++)
			star[i][j] = ' ';
	}

	Solve(0, 0, n);

	for (i = 0; i < n; i++) {
		for (j = 0; j < n; j++) {
			putchar(star[i][j]);
		}

		putchar('\n');
	}


	return 0;
}