#include <stdio.h>
#include <string.h>

int main() {
	char secret[501];
	int length;

	while (1) {
		fgets(secret, 501, stdin);

		if (!strncmp(secret, "END\n", 500))
			break;

		for (length = 0; secret[length]; length++);

		for (length -= 2; length >= 0; length--)
			putchar(secret[length]);

		puts("");
	}

	return 0;
}