#include <stdio.h>
#include <math.h>

int main() {
	int n, r, c, x, y, ans = 0;
	scanf("%d %d %d", &n, &r, &c);

	x = y = (int)pow(2, n) >> 1;

	while (n > 0) {
		int skip = x * y;

		if (r < y) {
			if (c >= x) {
				c -= x;
				ans += skip;
			}
		}

		else {
			if (c < x) {
				r -= y;
				ans += skip * 2;
			}

			else {
				r -= y;
				c -= x;
				ans += skip * 3;
			}
		}

		n--;
		x >>= 1;
		y >>= 1;
	}

	printf("%d\n", ans);
	return 0;
}