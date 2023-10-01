#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
	int i,j, k;
	int num, cnt=0;
	int x, y;

	int paper[100][100] = { 0 };

	scanf("%d", &num);
	for (i = 0; i < num; i++)
	{
		scanf("%d %d", &x, &y);
		for (k = x - 1; k < x - 1 + 10; k++)
			for (j = y - 1; j < y - 1 + 10; j++)
				if (paper[k][j] == 0)
					paper[k][j] = 1;
	}

	for (i = 0; i < 100; i++)
		for (k = 0; k < 100; k++)
			if (paper[i][k] == 1)
				cnt++;

	printf("%d", cnt);
	return 0;
}