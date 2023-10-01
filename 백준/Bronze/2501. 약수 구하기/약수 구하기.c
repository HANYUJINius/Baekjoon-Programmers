#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
	int num, cnt;
	int arr[1000] = { 0 };
	int arrIndex = 0;

	scanf("%d %d", &num, &cnt);

	for (int i = 1; i <= num; i++)
		if (num % i == 0)
			arr[arrIndex++] = i;

	if (arrIndex > cnt-1)
		printf("%d", arr[cnt-1]);
	else
		printf("0");

	return 0;
}