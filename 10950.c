#include <stdio.h>

int main() {
	int a = 0, b = 0, n = 0;
	scanf("%d", &n);

	while (n--) {
		scanf("%d %d", &a, &b);
		printf("%d\n", a + b);
	}

	return 0;
}