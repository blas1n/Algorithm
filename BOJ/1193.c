#include <stdio.h>

int numerator = 1, denominator = 1;

void UpNumerator() {
	numerator++;
	denominator--;
}

void UpDenominator() {
	numerator--;
	denominator++;
}

int IsTNum(int n) {
	int compareObj = 0, i;

	for (i = 1; n >= compareObj; i++) {
		if (n == compareObj)
			return 1;

		compareObj += i;
	}

	return 0;
}

int main() {
	int n, isUpDenominator = 1;
	scanf("%d", &n);

	for (int i = 1; i < n; i++) {
		if (IsTNum(i)) {
			if (isUpDenominator)
				denominator++;
			else
				numerator++;

			isUpDenominator = !isUpDenominator;
			continue;
		}

		if (isUpDenominator)
			UpDenominator();
		else
			UpNumerator();
	}

	printf("%d/%d", numerator, denominator);

	return 0;
}