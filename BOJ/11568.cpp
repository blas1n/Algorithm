#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	vector<int> v{ 100000000 };
	int n, x;
	cin >> n;

	while (n--) {
		cin >> x;
		
		if (v.back() < x)
			v.emplace_back(move(x));
		else
			*lower_bound(v.begin(), v.end(), x) = move(x);
	}
	
	cout << v.size();
	return 0;
}