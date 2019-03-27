#include <stdio.h>
#include <memory.h>

int main() {
	char s[21];
	int t, r;
	scanf("%d", &t);

	while (t--) {
		memset(s, 0, 21);
		scanf("%d %s", &r, s);

		for (int i = 0; s[i]; i++) {
			for (int j = 0; j < r; j++)
				printf("%c", s[i]);
		}

		puts("");
	}

	return 0;
}