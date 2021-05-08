# Lucas Numbers
Lucas numbers are numbers of the Lucas Sequence where L(n) = L(n-1) + L(n-2), L(0) = 2, L(1) = 1.

Sorce: https://oeis.org/A000032

## What does the script do?
The script prints Lucas numbers on the command line.

## `lucasNumbers.py` :
This script is ready to use script which uses one argument. The argument is the integer passed for the number of Lucas numbers in the sequence to be printed.
### lucas_numbers:
Function prints numbers divided by a space character.  
Invoking the script runs this function.
### lucas_numbers_last:
Function prints numbers divided by a space character and 
the time taken for the calculation.
## Installing the dependencies

### Used packages
This script require the sys and doctest package.

## How to use it
#### 1. Clone this repository:
```zsh
$> git clone https://github.com/StokicDusan/Python-misc.git
$> cd Python-misc/LucasNumbers/
```
#### 2. Launch:
In the command line simply invoke the script:
```zsh
$> python lucasNumbers.py argv1
```
* argv1:  
Any positive integer  

:warning: *Note:* Other input will result in an error


Invoking the script with no or less arguments will run testmod().