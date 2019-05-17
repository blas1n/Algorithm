long long sieve[10000000];

long long solution(int N) {
	long long answer = 0;

	for (int i = 2; i <= N; i++) {
		if (sieve[i]) continue;
		answer += i;

		for (int j = i; j <= N; j += i)
			sieve[j] = 1;
	}

	return answer;
}