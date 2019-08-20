## This program has been inspired by the following video from numberphile --> https://www.youtube.com/watch?v=pAMgUB51XZA  
Note that the code is not meant to be optimized but is just a way to quickly visualise the graphs shown in the video.  
Don't hesitate to submit a pull request if you have a more efficient code to find prime numbers.  
Requires matplotlib

Using the python library matplotlib, the program renders a scatter plot with the first n prime numbers on the x-axis.  
The plot follows the equation y = x - reverse(bin(x)) where bin(x) returns x in base 2 and reverse(string) returns the input string in reverse.  
Example: bin(131) = 10000011 and reverse('10000011') = '11000001'
