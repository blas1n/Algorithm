#include <iostream>

using namespace std;

int Calc(int n) {
	static int cache[1001] = { 0, 1, 2, };

	if (cache[n]) return cache[n];

	cache[n] = (Calc(n - 1) + Calc(n - 2)) % 10007;
	return cache[n];
}

int main() {
	int n;
	cin >> n;

	for (int i = 4; i < n; i++)
		Calc(i);

	cout << Calc(n) << endl;
	return 0;
}