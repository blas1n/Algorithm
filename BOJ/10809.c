#include <stdio.h>
#include <string.h>

#define MAX_LEN 100

int main() {
	char word[MAX_LEN] = { 0, };

	fgets(word, MAX_LEN, stdin);
	int len = strlen(word);

	for (char letter = 'a'; letter <= 'z'; letter++) {
		for (int i = 0; i <= len; i++) {
			if (i == len) {
				printf("-1 ");
				break;
			}

			if (word[i] == letter) {
				printf("%d ", i);
				break;
			}
		}
	}

	return 0;
}