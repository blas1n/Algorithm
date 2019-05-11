#include <stdio.h>
#include <memory.h>

int main() {
	int score[1000];
	int c, n, sum, winnerNum;
	float average;
	scanf("%d", &c);

	while (c--) {
		scanf("%d", &n);
		
		memset(score, 0, 1000 * sizeof(int));
		sum = winnerNum = 0;

		for (int i = 0; i < n; i++) {
			scanf("%d", &score[i]);
			sum += score[i];
		}

		average = (float)sum / n;

		for (int i = 0; i < n; i++) {
			if (score[i] > average)
				winnerNum++;
		}

		printf("%.3f%%\n", ((float)winnerNum / n) * 100);
	}

	return 0;
}