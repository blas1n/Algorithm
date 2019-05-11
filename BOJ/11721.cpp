#include <iostream>

using namespace std;

constexpr int MAXTILE = 1000;

int cache[MAXTILE + 1] = { 0, 1, 3, };

int Solution(int n) {
	if (cache[n])
		return cache[n];

	cache[n] = (Solution(n - 1) + (Solution(n - 2) * 2)) % 10007;

	return cache[n];
}

int main() {
	int n;
	cin >> n;

	for (int i = 1; i < n; i++)
		Solution(i);

	cout << Solution(n);
	return 0;
}