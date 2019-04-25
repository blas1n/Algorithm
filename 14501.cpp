#include <iostream>

using namespace std;

struct Counsel {
	int t;
	int p;
};

istream& operator>>(istream& is, Counsel& counsel) {
	is >> counsel.t >> counsel.p;
	return is;
}

Counsel counsels[15];
int cache[15];
int n;

int Solution(int day) {
	if (day >= n) return 0;

	if (cache[day])
		return cache[day];

	int p = (day + counsels[day].t <= n) ? counsels[day].p : 0;

	int lhs = p + Solution(day + counsels[day].t);
	int rhs = Solution(day + 1);

	cache[day] = (lhs > rhs) ? lhs : rhs;
	return cache[day];
}

int main() {
	cin >> n;

	for (int i = 0; i < n; i++)
		cin >> counsels[i];
	
	for (int i = n - 1; i > 0; i--)
		Solution(i);

	cout << Solution(0);
}