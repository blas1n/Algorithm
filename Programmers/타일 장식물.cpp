long long cache[81] = { 0, 4, 6, };

long long solution(int n) {
	if (cache[n])
		return cache[n];

	cache[n] = solution(n - 1) + solution(n - 2);
	return cache[n];
}
