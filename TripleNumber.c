#include <stdio.h>

void Swap(int* lhs, int* rhs) {
	int tmp = *lhs;
	*lhs = *rhs;
	*rhs = tmp;
}

int main() {
	int nums[3];
	scanf("%d %d %d", &nums[0], &nums[1], &nums[2]);

	for (int i = 0; i < 3; i++) {
		for (int j = i; j < 3; j++) {
			if (nums[i] < nums[j])
				Swap(&nums[i], &nums[j]);
		}
	}

	printf("%d", nums[1]);

	return 0;
}