#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
	int N;
	int cnt = 0;

	scanf("%d", &N);

	for (int i = 5; i <= N; i *= 5)
	{
		cnt += (N / i);
	}

	printf("%d", cnt);

	return 0;
}