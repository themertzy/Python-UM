

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

class calculator:
	
	def __init__(self):
		
		self.fuctioncalls = 0
	
	def add(self, a, b):
		
		return float(a + b)
	
	def subtract(self, a, b):

		return float(a-b)
	
	def multiply(self, a, b):

		return float(a*b)
	
	def divide(self, a, b):

		return float(a / b)
	
	def power(base, exp):
    		
		if(exp==1):
       			
			return base
   		 
		else:

			return(base*power(base,exp-1))
	
	def average(self, nums, total):

		if sum(nums) > 0:

			return float(sum(nums) / len(nums))
			
	def PyTheorem(self, a, b, c):
		
		if a and b != None and c == None
			
			return sqrt((a**2)+(b**2))
		
		elif a and c != None and b == None:

			return sqrt((c**2)-(a**2))
		
		elif b and c != None and a == None:

			return sqrt((c**2)-(b**2))
		
	def fibb(n):
	
		if n <= 1:
			
			return n
		
		else:
			
			return(fibb(n-1) + fibb(n-2))
		
	class area:                      #Nested class
		
		def __init__(self):
			
			self.DefineArea = None
			
		def triangle(b, h):

			return b*h*(1/2)

		def square(l, h):

			return l*h
		
		def parallelogram(b, h):
			
			return b*h
		
		def circle(vertradius, parradius):
			
			return None
		
