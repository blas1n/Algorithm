#include <stdio.h>

int main() {
	int score[1000] = { 0, };
	int n, m = 0;
	float sum = 0;
	scanf("%d", &n);

	for (int i = 0; i < n; i++) {
		scanf("%d", &score[i]);

		if (score[i] > m)
			m = score[i];
	}

	for (int i = 0; i < n; i++)
		sum += (float)score[i] / m * 100;
	
	printf("%f\n", sum / n);
	return 0;
}