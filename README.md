# An interesting graph involving prime numbers

This program aims to plot prime numbers in an interesting way.  
The plotting follow the equation y = x - decimal(reverse(binary(x))) where x is any prime number.  
```
  For x = 47:
  y = 47 - decimal(reverse(binary(47)))
  y = 47 - decimal(reverse(101111)) --> binary of 47 is 101111  
  y = 47 - decimal(111101) --> reverse of '101111' is '111101' (same as reading from right to left)  
  y = 47 - 61 --> decimal of 111101 if 61  
  y = -14
```

## How to use it

To clone the program on your local computer you can run 
```
'git clone https://github.com/TakanoriCodronAkieda/Prime-numbers-intersting-graph.git'
```
into the command line / terminal of your machine.

### Prerequisites

You will need Matplotlib in order to run this code.  
Matplotlib is a popular python library used to plot data.  
Here's a link to Matplotlib's official documentation: https://matplotlib.org/

### Installing Matplotlib

If you don't already have pip added to your environment PATH, I recommend that you watch the following tutorial: https://www.youtube.com/watch?v=emYR6vVHxp8  
If you have pip added to your environment PATH, you can simply run 'pip install matplotlib' to install the library.  


## Acknowledgments

The idea comes from this Numberphile video: https://www.youtube.com/watch?v=pAMgUB51XZA&t=491s

