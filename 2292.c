#include <stdio.h>

int main() {
	int n, ans;
	scanf("%d", &n);
	n--;

	if (n == 0) {
		printf("1\n");
		return 0;
	}

	for (ans = 1; n > (6 * ans); ans++)
		n -= 6 * ans;

	printf("%d", ans + 1);

	return 0;
}