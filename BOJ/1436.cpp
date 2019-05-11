#include <iostream>
#include <array>

using namespace std;

void Up(array<int, 8>& arr) {
	arr[7]++;

	for (int i = 7; i >= 0; i--) {
		if (arr[i] == 10) {
			arr[i - 1]++;
			arr[i] = 0;
		}
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	array<int, 8> arr = { 0, 0, 0, 0, 0, 6, 6, 6 };

	int n, v, i;
	cin >> n;

	while (n > 1) {
		Up(arr);

		for (i = 7; i > 2; i--) {
			if (arr[i] == 6 && arr[i - 1] == 6 && arr[i - 2] == 6) {
				n--;
				break;
			}
		}
	}

	for (v = 0; arr[v] == 0; v++);

	for (i = v; i < 8; i++)
		cout << arr[i];

	return 0;
}