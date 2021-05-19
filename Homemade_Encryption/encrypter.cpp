#include <iostream>
#include <string>
#include <stdlib.h>
#include <random>
#include <cmath>

bool isPrime(double n){
	//don't need to handle base case less then three
	//check if even
	//Miller-Rabin Primality Test
	if(fmod(n, 2) == 0){
		return false;
	}
	
	//write n as 2^r*d + 1 with d odd
	double d = n - 1;
	while(fmod(d, 2) == 0) {
		d = floor(d / 2);
	}
	//Witnessloop k times
	std::random_device rd;
	std::mt19937 mt(rd());
	std::uniform_real_distribution<double> dist(2, n - 1);
	for(int i = 0; i < 128; i++){
		double a = dist(mt);
		double x = fmod(pow(a, d), n);
		if(x != 1 and x!= n - 1){
			while(d != n - 1 and x != n - 1){
				x = fmod((x * x), n);
				d *= 2;
				if(x == 1){
					return false;
				}
			}
			if(x != n - 1){
				return false;
			}
		}
	}
	//prime
	return true;
}

int generateNBitNum(unsigned int n){
	if (n > 64){
		n = 64;
	}

	std::default_random_engine generator;
	std::uniform_real_distribution<double> dist(std::pow(2, (n-1)) + 1, std::pow(2, n));


	//generate number from 2**(n-1) + 1
	double num = 4;
	while(!isPrime(num)){
		num = dist(generator);
		std::cout << num << std::endl;
	}
		return num;
}


int main() {
	//std::string file_name;
	
	//get file name from the user 
	//std::cout << "Please enter the file which you would like to encrypt: "; 
	//std::cin >> file_name;155708393user@user-VirtualBox
	//generate two random prime numbers
	std::cout.precision(32);
	double prime1 = generateNBitNum(64);
	std::cout << prime1 << std::endl;
	

	return 0;
}