#include <stdio.h>

int fac(int n) {
	int ans = 1;

	for (int i = 2; i <= n; i++)
		ans *= i;

	return ans;
}

int main() {
	int n;
	scanf("%d", &n);

	printf("%d\n", fac(n));
	return 0;
}