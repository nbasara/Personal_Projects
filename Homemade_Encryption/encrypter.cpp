#include <iostream>
#include <string>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include <fstream>
#include <vector>

//calculate the greatest common divisor of two nunbers
unsigned long long int gcd(unsigned long long int a, unsigned long long int b){
	unsigned long long int temp;
	while(true){
		temp = fmod(a, b);
		if(temp == 0){
			return b;
		}
		a = b;
		b = temp;
	}
}

unsigned long long int lcm(unsigned long long int a, unsigned long long int b){
	return (a*b)/gcd(a, b);
}

//calulating (base^exp) % mod
unsigned long long int power(unsigned long long int base, unsigned long long int exp, unsigned long long int mod){
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

//test to check the primality of the number
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

//calculates d such that e*d = 1 mod totient
unsigned long long int modInverse(unsigned long long int a, unsigned long long int m){ 
    unsigned long long int m0 = m;
    unsigned long long int y = 0, x = 1;
	if (m == 1)
        return 0;
 
    while (a > 1) {
        // q is quotient
        unsigned long long int q = a / m;
        unsigned long long int t = m;
 
        // m is remainder now, process same as
        // Euclid's algo
        m = a % m, a = t;
        t = y;
 
        // Update y and x
        y = x - q * y;
        x = t;
    }
 
    // Make x positive
    if (x < 0)
        x += m0;
 
    return x;
}

//function to tell when a number is prime
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

//generates an n bit number
//is capable of 64 bit numbers the limit of c++
//function takes too long to return a value
//generally 32 bit numbers are too large to work with
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

//given a file it will decrypt the mesaage with private keys
void RSA_decryption(double d, double n, std::string target){
	double i;
	double m;
	//open encrypted binary file
	std::fstream input(target,std::ios_base::in);

	//unload the characters into the buffer
	//open file write 
	std::ofstream out;
	out.open("Decyrption.txt");
	//iterate through the buffer
	std::cout << d << " " << n << std::endl;
	while(input >> i){
		std::cout << i << " ";
		m = power(i, d, n);
		std::cout << m << std::endl;
	}

	out.close();
	input.close();

}

//given two prime numbers it will encrypt a text file
void RSA_encrypt(double p, double q, std::string file){
	double n, e, d, c, totient, m;
	n = p * q;
	totient = (p - 1)*(q - 1);
	std::cout << "This is my phi " << totient << std::endl;
	e = 17;

	while(e < totient){
		double track = gcd(e, totient);
		if(track == 1){
			break;
		} else {
			e++;
		}
	}
	std::cout << "This is my e " << e << std::endl;
	d = modInverse(e, totient);
	std::cout << "This the private key generated for keeps " << d << std::endl;
	//This is where the program reads the file to encrypt the message
	//open file to read the message
	std::ifstream fd(file);
	//File to write encrypted message
	std::ofstream out;
	out.open("Encryption.txt");
	if(fd.is_open()){
		//read each character of file and transform to int
		std::vector<unsigned char> buffer(std::istreambuf_iterator<char>(fd), {});
		for(unsigned char m : buffer){
			c = (double) m;
			c = power(c, e, n);
			out << c << " ";
		} 
		out.close();
		fd.close();
	} else{
		std::cerr << "ERROR, Was unable to open file: " << file << std::endl;
	}
	RSA_decryption(d, n, "Encryption.txt");

}


int main() {
	std::string file_name = "Test.txt";
	unsigned long long int prime1, prime2; 	
	//set random seed
	srand(time(NULL));
	
	//get file name from the user 
	//std::cout << "Please enter the file which you would like to encrypt: "; 
	//std::cin >> file_name;
	//generate two random prime numbers
	prime1 = generateNBitNum(6);
	prime2 = generateNBitNum(6);
	//Run the RSA algorithm
	RSA_encrypt(prime1, prime2, file_name);

	return 0;
}
