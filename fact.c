#include <stdio.h>


unsigned long long int factorial(unsigned int n)
{
	if (n == 0)
		return 1;
	return n * factorial(n - 1);
}

int main()
{
	int num = 60;
	unsigned long long int ans;
	for (int i = 0; i<10000000; i++)
	{
		ans = factorial(num);
	}
	
	printf("Factorial of %d is %llu", num, ans);
	printf("\n");
	return 0;
}

