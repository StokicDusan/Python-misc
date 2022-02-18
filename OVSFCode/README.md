# OVSF Code Tree

The OVSF Code Tree generates an OVSF code from a set of orthogonal codes. OVSF codes were first introduced for 3G communication systems. OVSF codes are primarily used to preserve orthogonality between different channels in a communication system.

OVSF codes are defined as the rows of an N-by-N matrix, CN, which is defined recursively as follows. First, define C1 = [1]. Next, assume that CN is defined and let CN(k) denote the kth row of CN.

The OVSF codes can also be defined recursively by a tree structure, as shown in the following figure:

![ovsf-dark-graph](/OVSFCode/An-orthogonal-variable-spreading-factor-OVSF-code-tree-dark.png#gh-dark-mode-only)  
![ovsf-light-graph](/OVSFCode/An-orthogonal-variable-spreading-factor-OVSF-code-tree-light.png#gh-light-mode-only)

## Parameters
Running VolsovoStablo.py you choose to save the codes in a text file or print it in the terminal. After the first option, you are presented with choosing the spread factor.  
Spreading factor (SF): Positive integer that is a power of 2, specifying the length of the code.

## Example
Following picture shows an example of running the script:

![ovsf-example](/OVSFCode/example1.png) 
