#include <stdio.h>

int main() {
	int E, S, M, e, s, m, ret = 0;
	scanf("%d %d %d", &E, &S, &M);
	e = s = m = 1;

	while (++ret) {
		if ((E == e) && (S == s) && (M == m))
			break;

		e %= 15;
		s %= 28;
		m %= 19;
		e++; s++; m++;
	}

	printf("%d\n", ret);
	return 0;
}