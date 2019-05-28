#include <cstdio>
#include <list>
#include <algorithm>

using namespace std;

int arr[500000];
list<int> beforeIndex[1000000];

int main() {
	int n;
	scanf("%d", &n);

	for (int i = 0; i < n; i++) {
		scanf("%d", arr + i);
		beforeIndex[arr[i]].push_back(i);
	}

	sort(arr, arr + n);

	int diff, max = 0;

	for (int i = 0; i < n; i++) {
		diff = beforeIndex[arr[i]].front() - i;
		beforeIndex[arr[i]].pop_front();
		if (diff > max) max = diff;
	}

	printf("%d\n", max + 1);
	return 0;
}