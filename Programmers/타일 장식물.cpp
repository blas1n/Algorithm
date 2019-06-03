#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

long long cache[81] = { 0, 4, 6, };

long long fib(int n) {
	if (cache[n])
		return cache[n];

	cache[n] = fib(n - 1) + fib(n - 2);
	return cache[n];
}

long long solution(int N) {
	vector<int> a;
	initializer_list
	initializer_list<int>(a);
	return solution(N);
}
