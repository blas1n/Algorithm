#include <stdio.h>
#include <stdlib.h>

int arr[5000000];

int cmp(void* pLhs, void* pRhs) {
	int lhs = *(int*)pLhs;
	int rhs = *(int*)pRhs;

	if (lhs > rhs)
		return 1;
	if (lhs < rhs)
		return -1;
	return 0;
}

int main() {
	int n, k;
	scanf("%d %d", &n, &k);

	for (int i = 0; i < n; i++) {
		scanf("%d", arr + i);
	}

	qsort(arr, n, sizeof(int), cmp);

	printf("%d\n", arr[k - 1]);
	return 0;
}