#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
	int i, j, num;
	int arr[9][9] = { 0 };
	int max = arr[0][0];
	int iIndex = 0;
	int jIndex = 0;


	for (i = 0; i < 9; i++)
		for (j = 0; j < 9; j++)
		{
			scanf("%d", &arr[i][j]);
			if (arr[i][j] > max)
			{
				max = arr[i][j];
				iIndex = i;
				jIndex = j;
			}
		}

	printf("%d\n%d %d", max, iIndex+1, jIndex+1);
			
	return 0;
}