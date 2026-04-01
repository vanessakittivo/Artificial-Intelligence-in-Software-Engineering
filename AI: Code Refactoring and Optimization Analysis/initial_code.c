#include <stdio.h>

/**
 * print_to_98 - prints all natural numbers from n to 98
 * @n: starting number
 *
 * Return: void
 */
void print_to_98(int n)
{
	int i;

	if (n <= 98)
	{
		for (i = n; i <= 98; i++)
		{
			if (i != n)
				printf(", ");
			printf("%d", i);
		}
	}
	else
	{
		for (i = n; i >= 98; i--)
		{
			if (i != n)
				printf(", ");
			printf("%d", i);
		}
	}
	printf("\n");
}
