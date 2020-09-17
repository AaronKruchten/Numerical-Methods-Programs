##############################################
#First Computational Problem
##############################################
def bisection_algorithm(a,b,iterations,method):
	polynomial = lambda x: ((x+2)*x + 10)*x -20
	if(polynomial(a) < 0):
		sign_a = -1
		sign_b = 1
	else:
		sign_a = 1
		sign_b = 1
	for i in range(iterations):
		if(method == "standard"):
			c = standard_method(a,b)
		elif(method == "falsi"):
			c = regula_falsi(a,b)
		elif(method == "modified"):
			c = modified_regula_falsi(a,b)
		if(polynomial(c) == 0):
			return c
		elif(polynomial(c) < 0):
			if(sign_a == -1):
				a = c
			else:
				b = c
		elif(polynomial(c) > 0):
			if(sign_a == 1):
				a = c
			else:
				b = c
	return(c)



#returns midpoint
def standard_method(a,b):
	return (1/2)*(a+b)


def regula_falsi(a,b):
	polynomial = lambda x: ((x+2)*x + 10)*x -20
	numerator = a*polynomial(b) - b*polynomial(a)
	denominator  = polynomial(b) - polynomial(a)
	return(numerator/denominator)

def modified_regula_falsi(a,b):
	polynomial = lambda x: ((x+2)*x + 10)*x -20
	f_a = polynomial(a)
	f_b = polynomial(b)
	if(f_a*f_b < 0):
		numerator = a*f_b - 2*f_a*b
		denominator = f_b - 2*f_a
		return(numerator/denominator)
	else:
		numerator = 2*a*f_b - f_a*b
		denominator = 2*f_b - f_a


#STANDARD AFTER 5 ITERATIONS
1.34375

#FALSI AFTER 5 ITERATIONS
1.368756579007422

#MODIFIED FALSE AFTER 5 ITERATIONS
1.3716732503750129

##############################################
#Second Computational Problem
##############################################

#Python float type is double precision
#at x = 2 polynomial equals -1, so that seems like a reasonable starting point
def newton_method(x,delta):
	function = lambda x : (x**2 -2)*x - 5
	derivative = lambda x : 3*x**2 - 2
	while(abs(function(x)) >= delta):
		x = x- function(x)/derivative(x)
	return x

#ANSWER APPROXIMATELY:
2.0945514815423265



