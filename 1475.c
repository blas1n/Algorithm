#include <stdio.h>

int main() {
	char n[8] = { 0, };
	int overlapNum, turnNum, isTurnNum, ans = 0;
	scanf("%s", &n);

	for (int i = 0; n[i]; i++) {
		overlapNum = 0;
		turnNum = 0;

		if (n[i] == '6' || n[i] == '9')
			isTurnNum = 1;
		else
			isTurnNum = 0;

		for (int j = i + 1; n[j]; j++) {
			if (isTurnNum) {
				if (n[j] == '6' || n[j] == '9') {
					turnNum++;

					if (turnNum == 2) {
						turnNum = 0;
						overlapNum++;
					}

					continue;
				}
			}

			if (n[i] == n[j])
				overlapNum++;
		}

		ans = overlapNum > ans ? overlapNum : ans;
	}

	printf("%d\n", ans + 1);
	return 0;
}