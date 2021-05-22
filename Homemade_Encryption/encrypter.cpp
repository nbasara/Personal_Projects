#include <iostream>
#include <string>
#include <stdlib.h>
#include <time.h>
#include <cmath>

//calculate the greatest common divisor of two nunbers
unsigned long long int gcd(unsigned long long int a, unsigned long long int b){
	unsigned long long int temp;
	while(true){
		temp = a % b;
		if(temp == 0){
			return b;
		}
		a = b;
		b = temp;
	}
}

//calulating (base^exp) % mod
int power(unsigned long long int base, unsigned long long int exp, unsigned long long int mod){
	//initial result
	unsigned long long int res = 1;
	base = base % mod;

	while(exp > 0){
		//if y is odd, mult x with result
		if(exp & 1){
			res = (res*base) % mod;
		}
		//y is even....y = y/2
		exp = exp>>1;
		base = (base*base) % mod;
	}
	return res; 
}

bool millerTest(unsigned long long int n, unsigned long long int d, int max){
	//pick a random intger from a in range [2, n -2]
	unsigned long long int a = rand() % (n - 2) + 2;
	unsigned long long int x = power(a, d, n);
	if(x == 1 || x == (n - 1)){
		//prime
		return false;		
	}
	for(int i = 0; i < max; i ++){
		x = (x*x) % n;
		d *= 2;
		if(x == n - 1){
			//prime
			return false;
		}
		if(x == 1){
			//composite
			return true;
		}
	}
	//composite
	return true;

}

//tells if the gcd of two numbers is 1
bool isCoprime(unsigned long long int a, unsigned long long int b){
	if(gcd(a, b) == 1){
		return true;
	} else {
		return false;
	}
}

bool isPrime(unsigned long long int num){
	//don't need to handle base case less then three
	//check if even
	//Miller-Rabin Primality Test
	
	//write n as 2^r*d + 1 with d odd
	unsigned long long int d = num - 1;
	unsigned long long int max_divisions = 0;
	while(d % 2 == 0) {
		d = d / 2;
		max_divisions++; 
	}
	//Witnessloop k times
	for(int i = 0; i < 128; i++){
		if(millerTest(num, d, max_divisions)){
			//not prime
			return false;
		}
	}
	//prime
	return true;
}

unsigned long long int generateNBitNum(int n){
	if (n > 64){
		n = 64;
	}
	//generate number from 2**(n-1) + 1
	unsigned long long int num =  rand() % (((unsigned long long int) std::pow(2, n)) - 1) + (((unsigned long long int) std::pow(2, (n-1))) + 1);
	while(!isPrime(num)){
		num = rand() % (((unsigned long long int) std::pow(2, n)) - 1) + (((unsigned long long int) std::pow(2, (n-1))) + 1);
	}
	return num;
}

void RSA(unsigned long long int p, unsigned long long int q){
	unsigned long long int n, totient, e, d;
	n = p * q;
	totient = (p - 1)*(q - 1);

	e = rand() % (totient) + 1;

	while(!isCoprime(e, totient)){
		e = rand() % (totient) + 1;
	}
	d = (2 * totient + 1) / e;
	//This is where the program reads the file to encrypt the message
}


int main() {
	//std::string file_name;
	unsigned long long int prime1, prime2; 	
	//set random seed
	srand(time(NULL));
	
	//get file name from the user 
	//std::cout << "Please enter the file which you would like to encrypt: "; 
	//std::cin >> file_name;155708393user@user-VirtualBox
	//generate two random prime numbers
	prime1 = generateNBitNum(32);
	std::cout << prime1 << std::endl;
	prime2 = generateNBitNum(32);
	std::cout << prime2 << std::endl;
	RSA(prime1, prime2);

	return 0;
}