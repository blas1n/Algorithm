#include <stdio.h>

int main() {
	char str[101];
	fgets(str, 101, stdin);

	putchar(str[0]);

	for (int i = 1; str[i]; i++) {
		if (str[i] == '-')
			putchar(str[i + 1]);
	}

	return 0;
}