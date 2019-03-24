#include <stdio.h>
#include <memory.h>

int main() {
	int element[3];
	int n, copy, ret = 0;
	scanf("%d", &n);

	for (int i = 1; i <= n; i++) {
		if (i < 100) {
			ret++;
			continue;
		}

		if (i == 1000) break;

		copy = i;
		for (int j = 0; copy > 0; j++) {
			element[j] = copy % 10;
			copy /= 10;
		}

		if ((element[0] - element[1]) == (element[1] - element[2]))
			ret++;
	}

	printf("%d\n", ret);
	return 0;
}