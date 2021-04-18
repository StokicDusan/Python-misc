# Count Primes

A script for printing and/or counting prime numbers.

## What does the script do?
The script calculates primes using the sieve of eratosthenes and count how many there are. 
It displays the number of Mersenne, Twin, Cousin, Sexy and Pythagorean primes.

## `countPrimes.py` :
This script is ready to use script which uses two arguments to run. The first argument decides what will be displayed and the second decides the upper bound for the search (including that number).


## Installing the dependencies

### Used packages
This script require the time, math and sys package.

## How to use it
#### 1. Clone this repository:
```zsh
$> git clone https://github.com/StokicDusan/Python-misc.git
$> cd Python-misc/CountPrimes/
```
#### 2. Launch:
In the command line simply invoke the script with two arguments:
```zsh
$> python countPrimes.py argv1 argv2
```
```
* argv1:
    1 - print primes
    2 - count primes
    3 - both
    Note: Other input will result in an error

* argv2:
    Any positive integer
    Note: Other input will result in an error
```