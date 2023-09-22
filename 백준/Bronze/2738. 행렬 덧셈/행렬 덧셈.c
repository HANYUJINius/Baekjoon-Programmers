#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
	int a, b, i, j;

	int arr[100][100] = { 0 };
	int brr[100][100] = { 0 };
    int sum[100][100] = { 0 };

	scanf("%d %d", &a, &b);

	for (i = 0; i < a; i++)
		for (j = 0; j < b; j++)
			scanf("%d", &arr[i][j]);
    
    for (i = 0; i < a; i++)
		for (j = 0; j < b; j++)
			scanf("%d", &brr[i][j]);

	for (i = 0; i < a; i++)
		for (j = 0; j < b; j++)
			sum[i][j] = arr[i][j] + brr[i][j];

	for (i = 0; i < a; i++)
	{
		for (j = 0; j < b; j++)
			printf("%d ", sum[i][j]);
		printf("\n");
	}
	return 0;
}
