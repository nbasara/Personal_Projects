# File Encryptor
## Created by
## Nathan Basara
**Main Idea**
Encrypt a file using RSA algorithm. Generate two random prime numbers between ~~1,000,000 and 1,000,0000,000~~ 100,000 and 10,000.  *The program was generating prime numbers but was taking to long to do so.*   Verify the prime numbers using Miller-Rabin and Solovay-Strassen. Write tests for the program.  Possibily add in a bit shifter that can be chosen from arguements to the program.

*To do*
- [X] Generate Two Random Prime Numbers (for small numbers)
- [X] Verify primality (for small numbers)
- [ ] Generate multiple threads to generate candidates and check if they are prime
- [ ] Implement RSA
- [ ] Open file to encrypt
- [ ] Write Encrypted message
- [ ] Give user keys
- [ ] Decrypt files

**TBD**
- What is a fast way to generate large prime numbers?
- Am I writing over the file or generating a new one?
- Seperate program to decrypt or create option menu?
- Different options to shift the original bits?

*Update*
The initial algorithm of generating random int and testing if it was prime was **A** taking too long to generate a prime number and **B** not generating a guarenteed n-bit number.

I will instead be generating an n bit checking if divisible by any prime < 400 and then verifying against 20 iterations of the MillerRabin primality test.

Slowly realized doing this single threaded will not result in progress.  Time to use multiple threads.
