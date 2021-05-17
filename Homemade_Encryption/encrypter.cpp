#include <iostream>
#include <string>
#include <stdlib.h>
#include <time.h>
#include <cmath>

//calulating (base^exp) % mod
int power(int base, unsigned int exp, int mod){
	//initial result
	int res = 1;
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

bool millerTest(int n, int d){
	//pick a random intger from a in range [2, n -2]
	int a = rand() % (n - 2) + 2;
	int x = power(a, d, n);
	if(x == 1 || x == (n - 1)){
		//prime
		return true;		
	}
	while(d != n - 1){
		x = (x*x) % n;
		d *= 2;
		if(x == n - 1){
			//prime
			return true;
		}
		if(x == 1){
			//composite
			return false;
		}
	}
	//composite
	return false;

}

bool isPrime(int num){
	//don't need to handle base case less then three
	//check if even
	//Miller-Rabin Primality Test
	if(num % 2 == 0){
		return false;
	}
	else if(num % 5 == 0){
		return false;
	}
	//write n as 2^r*d + 1 with d odd
	int d = num - 1;
	while(d % 2 == 0) {
		d = d / 2; 
	}
	//Witnessloop k times
	for(int i = 0; i < 4; i++){
		if(!millerTest(num, d)){
			//not prime
			return false;
		}
	}
	//prime
	return true;
}

int generatePrime(){
	int n;

	//generate number  from 1,000,000 to 1,000,000,000
	n = rand() % 1000000 + 100000;

	//check if a prime number
	while(!isPrime(n)){
		n = rand() % 1000000000 + 1000000;
	}
	return n;
}

int main() {
	std::string file_name;

	//set random seed
	srand(time(NULL));
	
	//get file name from the user 
	//std::cout << "Please enter the file which you would like to encrypt: "; 
	//std::cin >> file_name;155708393user@user-VirtualBox

	//generate two random prime numbers
	int prime1 = generatePrime();
	std::cout << prime1 << std::endl;
	int prime2 = generatePrime();
	std::cout << prime2 << std::endl;

	return 0;
}