#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
	int i, j;
	char arr[5][15] = { 0 };

	for (i = 0; i < 5; i++)
			scanf("%s", arr[i]);

	for (i = 0; i<15; i++)
		for (j = 0; j<5; j++)
		{
			if (arr[j][i] == '\0')
				continue;
			else
				printf("%c", arr[j][i]);
		}

	return 0;
}