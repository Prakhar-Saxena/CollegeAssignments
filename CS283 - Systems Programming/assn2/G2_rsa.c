#include <stdlib.h>
#include <math.h>
#include <stdbool.h>
#include <stdio.h>

int GCD(int a, int b){
	
	//everything divides 0
	if (a == 0 || b == 0){
		return 0;
	}
	
	//base case
	if (a == b){
		return a;
	}

	//a is greater
	if (a > b){
		return GCD(a-b, b);
	}
	
	return GCD(a, b-a);
}

// int coprime(int x){
// 	do {
// 	int r = rand();
// 	}
// 	while ( GCD(x, r) == 1)	

//  return r;
// }

bool isCoprime(int x, int y){
	if(GCD(x,y) == 1){
		return true;
	}
	else{
		return false;
	}
}

int modulo(int a, int b, int c){
	int x = a^b;
	int mod = x % c;
	return mod;
}

// int mod_inverse(int base, int m){
// 	double inverse = (1 / base);
// 	// long inverse = pow(base, -1);
// 	double mod_inverse = inverse % m;

// 	return mod_inverse;
// }

int mod_inverse(int a, int m)
{
    a = a%m;
    for (int x=1; x<m; x++)
       if ((a*x) % m == 1)
          return x;
}

int totient(int n){

	long result = 1;
	for(int i = 2; i < n; i++)
		if(GCD(i, n) == 1)
			result++;
	return result;

}


// int findPrime(int m){
// 	int check = 0;
// 	int c = 0;

// 	int i = 0;

// 	for(i = 2; i<= 1000; i++){
// 		for(int j = 2; j<= i/2; j++){
			
// 			if(i%j == 0)
// 			{
// 				check = 1;
// 				break;
				
// 			}
		
// 		}
// 	}
	
// 	if(check == 0){
// 		c++;
// 		if(c == m){
// 			return i;
// 		}
	
// 	}
// }

int findPrime(int n)
{
	int a,b,d,c=0;
	for(a=2;a<=1000;a++)
	{
		d=0;
		for(b=2;b<=a/2;b++)
		{
			if(a%b==0)
			{
				d=1;
				break;
			}
		}
		if(d==0)
			c++;
		if(c==n)
		{
			return a;
			break;
		}
	}

}


// int endecrypt(int msg_or_cipher, int key, int c){
	
// 	int m = 0;
// 	int n = 0;
// 	int prime_one = 0;
// 	int prime_two = 0;

// 	printf("Enter the mth prime and the nth prime number\n");
// 	scanf("%d", m);
// 	scanf("%d", n);
	
// 	prime_one = findPrime(m);
// 	prime_two = findPrime(n);
	
// 	int c = prime_one * prime_two;
// 	int m = (prime_one-1) * (prime_two-1);



// }

int endecrypt(int msg, int e, int c){
	int mod = modulo(e, 1, c);
	int res = msg ^ mod;
	return res;
}

int main(){
	int p = 0;
	int q = 0;
	int prime_one = 0;
	int prime_two = 0;

	printf("Enter the mth prime and the nth prime number\n");
	scanf("%d%d", &p, &q);
	printf("prime1:  %d\nprime2:  %d\n",findPrime(p),findPrime(q));
	prime_one = findPrime(p);
	prime_two = findPrime(q);
	
	int c = prime_one * prime_two;
	int m = (prime_one-1) * (prime_two-1);

	int e = m * 2;

	while (true){
		if ( isCoprime(e,c) && isCoprime(e,m) && (modulo(e, 1, m) > 1) ){
			break;
		}
		else{
			e++;
		}
	}

	int d = mod_inverse(1, modulo(e, 1, m) );

	printf("c: %d\nm:  %d\ne: %d\nd: %d\n", c, m, e, d);

	printf("Please enter the public key (e, c): first e, then c\n");

	int pub_e, pub_c;

	scanf("%d%d", &pub_e, &pub_c);

	printf("Please enter a sentence to encrypt\n");

	char msg[];

	scanf("%s", &msg);

	int en = endecrypt((int)msg ,pub_e, pub_c);
	printf("%d\n", en);

	// for(int i = 0; i < strlen(msg); i++){
	// 	int en = endecrypt(msg[i] ,pub_e, pub_c);
	// 	printf("%d\n", en);
	// }

	return 0;
}
