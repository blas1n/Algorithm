int sieve[1000001];

int solution(int n) {
	int answer = 0;

	for (int i = 2; i <= n; i++) {
		if (sieve[i]) continue;
		answer++;

		for (int j = i; j <= n; j += i)
			sieve[j] = 1;
	}

	return answer;
}