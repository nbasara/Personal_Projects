#include <iostream>
#include <string>
#include <stdlib.h>
#include <time.h>
#include <cmath>

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
	for(int i = 0; i < 7; i++){
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


int main() {
	//std::string file_name;

	//set random seed
	srand(time(NULL));
	
	//get file name from the user 
	//std::cout << "Please enter the file which you would like to encrypt: "; 
	//std::cin >> file_name;155708393user@user-VirtualBox
	//generate two random prime numbers
	unsigned long long int prime1 = generateNBitNum(64);
	std::cout << prime1 << std::endl;
	unsigned long long int prime2 = generateNBitNum(64);
	std::cout << prime2 << std::endl;
	

	return 0;
}