#include <iostream>
#include <stack>

using namespace std;

int main() {
	stack<int> stack;
	int k, n;
	cin >> k;

	while (k--) {
		cin >> n;

		if (n != 0)
			stack.push(n);
		else
			stack.pop();
	}

	int result = 0;

	while (!stack.empty()) {
		result += stack.top();
		stack.pop();
	}

	cout << result << endl;
	return 0;
}