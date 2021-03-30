#include <stdio.h>
#include <assert.h>

double avg(double a[], int n)
{
	int i;
	double sum;

	assert(n > 0);
	sum = 0.0;
	for (i=0;i<n;i++)
		sum += a[i];
	return sum/n;
}

int main(int argc, char *argv[])
{
	double a[5] = {1.0,2.0,3.0,4.0,5.0};
	int n;

	if( argc > 1 )
		printf( "Got an arg: %s\n\n", argv[1] ) ;

	printf("Enter size:  ");
	scanf("%d",&n);
	assert(n<5);
	printf("Avg. = %f\n", avg(a,n));
}
