

#Fibonacci Sequence Function using Recursion

def fibb_recur(n):
	
	if n <= 1:
		return n
	else:
		return(fibb_recur(n-1) + fibb_recur(n-2))

##################################################################################################################################################################################

#A Fibonacci Sequence Function using iteration.  Iteration is often considered to be slower than a recursive approach.

def fib_iteration(n):
    
	a = 0
	b = 1
    
	for i in range(0, n):
        	temp = a
        	a = b
        	b = temp + b
		
    	return a
	
##################################################################################################################################################################################	

