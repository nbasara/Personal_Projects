#include <iostream>
#include <string>
#include <stdlib.h>
#include <time.h>

bool millerTest(int n, int d){
	return true;
}

bool isPrime(int num){
	//don't need to handle base case less then three
	//check if even
	if(num % 2 == 0){
		return false;
	}
	//find odd number less n
	int d = num - 1;
	while(d % 2 == 0) {
		d = d / 2; 
	}
	for(int i; i < 6; i++){
		if(millerTest(n, d)){
			return false;
		}
	}
	return true;
}

int generatePrime(){
	int n;

	//generate number  from 1,000,000 to 1,000,000,000
	n = rand() % 1000000000 + 1000000;

	//check if a prime number
	if (isPrime(n)) {
		return n;
	} else {
		return generatePrime(); // try to generate another
	}
}

int main() {
	std::string file_name;

	//set random seed
	srand(time(NULL));
	
	//get file name from the user 
	std::cout << "Please enter the file which you would like to encrypt: "; 
	//std::cin >> file_name;

	//generate two random prime numbers
	int prime1 = generatePrime();
	int prime2 = generatePrime();

	std::cout <<"These are the two random numbers generated " << prime1
		<< "\t" << prime2 << std::endl;


	return 0;
}