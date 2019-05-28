#include <stdio.h>

int main() {
	int n;
	scanf("%d", &n);

	for (int i = 2; n > 1; i++)
		if ((n % i) == 0) {
			printf("%d\n", i);
			n /= i--;
		}

	return 0;
}