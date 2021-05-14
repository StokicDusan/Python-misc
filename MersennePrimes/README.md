# Mersenne Primes

A Mersenne prime is a prime number that is one less than a power of two. That is, it is a prime number of the form <img src="https://latex.codecogs.com/gif.latex?\bg_white&space;M_{n}=2^{n}-1" title="M_{n}=2^{n}-1" /> for some integer n.

## What does the script do?
The script prints Mersenne prime numbers on the command line.

## `mersennePrimes.py` :
This script is ready to use script which uses one arguments to run. The argument is the integer passed for the number of primes to be printed.

### mersenne_primes:
Function prints numbers divided by a space character.  
Invoking the script runs this function.

### mersenne_primes_format:
Function prints every number in a new line formatted to display in the <img src="https://latex.codecogs.com/gif.latex?\bg_white&space;2^{n}-1" title="2^{n}-1" /> form as well.

## Installing the dependencies

### Used packages
This script require the math, doctest and sys package.

## How to use it
#### 1. Clone this repository:
```zsh
$> git clone https://github.com/StokicDusan/Python-misc.git
$> cd Python-misc/MersennePrimes/
```
#### 2. Launch:
In the command line simply invoke the script with one argument:
```zsh
$> python mersennePrimes.py argv1
```
* argv1:  
Any positive integer  

:warning: *Note:* Other input will result in an error


Invoking the script with no arguments will run testmod().
