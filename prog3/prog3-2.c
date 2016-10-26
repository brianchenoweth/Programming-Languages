#include <stdio.h>


int main (int argc, char**argv)
{
	char b;
	scanf("%c", &b);
	printf("%d\n", b-argv[1][0]);
	return 0;
	}
