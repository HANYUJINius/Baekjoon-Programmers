#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int numSum(int n);
void printNum(int n, int cnt);

int main(void)
{
	int num,k;

	while (1)
	{
		scanf("%d", &num);
		if (num == -1)
			break;
		k = numSum(num);
		if (k)
			printNum(num,k);
		else
			printf("%d is NOT perfect.\n", num);
	}
	return 0;
}

int numSum(int n)
{
	int sum = 0,cnt =0;
	for (int i = 1; i < n; i++)
		if (n % i == 0)
		{
			sum += i;
			cnt++;
		}

	if (sum == n)
		return cnt;
	return 0;
}

void printNum(int n, int cnt)
{
	int index=0;

	printf("%d = ", n);

	for (int i = 1; i < n; i++)
		if (n % i == 0)
		{
			printf("%d", i);
			index++;
			if (index < cnt)
				printf(" + ");
		}
	printf(" ");
}