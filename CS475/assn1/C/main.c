#include <stdio.h>

#include"generate.h"

int main(int argc, char *argv[])
{
	int n = 7;
	int * nums = generate(n);
	for(int i = 0; i < sizeof(nums)/sizeof(nums[0]); i++){
		printf("%d", nums[i]);
	}
}
