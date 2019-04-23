#include <iostream>

using namespace std;

int Min(int lhs, int rhs) {
	return lhs < rhs ? lhs : rhs;
}

int Calc(int n) {
	static int cache[1000001] = { 0, };

	if (n == 1) return 0;
	if (cache[n]) return cache[n];

	int result = Calc(n - 1) + 1;

	if (n % 3 == 0) result = Min(result, Calc(n / 3) + 1);
	if (n % 2 == 0) result = Min(result, Calc(n / 2) + 1);

	cache[n] = result;
	return result;
}

int main() {
	int n;
	cin >> n;

	for (int i = 2; i < n; i++)
		Calc(i);

	cout << Calc(n) << endl;

	return 0;
}