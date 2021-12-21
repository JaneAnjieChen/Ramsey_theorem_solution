## Ramsey_theorem_solution
#### A solution to the Ramsey's theorem
In discrete mathematics, Ramsey’s theorem states that for any positive integer k, there is an integer m such that in any party with at least m guests, one of the following statements must be true:  
1. There are at least k guests who know each other.
2. There are at least k guests who do not know each other.  
For example, for k = 3, then in any party of at least 6 guests, either there are three guests who know each other, or there are three guests who do not know each other.  

This question asks you to write a program (using either Python, C, C++ or Java) to help verify Ramsey’s theorem. The input of the program is organized as follows:  
- The first line of the input has an integer m, followed by m lines of string, each
representing a guest (so there are totally m guests for this input).
- Then, there is another line of integer n, followed by n lines of pair of guests (guest a and guest b know each other if and only if there is a line of pair a, b in the input).
- Then, there is a line containing an integer k.  
For the output, your program should print a set of k guests who knows each other, and if there is no such set, the program should print a set of k guests who do not know each other.
