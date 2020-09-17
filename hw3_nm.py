import numpy as np 
import math



#####################################
#COMPUTATIONAL EXERCISE 1
#####################################
def newton_method(x_1,x_2,iterations):
	fun_one = lambda x_1,x_2 : x_1**2 + 2*x_2 - 2
	fun_two = lambda x_1,x_2 : x_1 + 4*x_2**2 - 4
	for i in range(iterations):
		a = 2*x_1
		d = 8*x_2
		inverse_jacobian =  np.matrix([[d,-2],[-1,a]])
		scalar = 1/(a*d - 2)
		x_n_vec = np.array([[x_1],[x_2]])
		f_x_n_vec = np.array( [[fun_one(x_1,x_2)],[fun_two(x_1,x_2)]])
		new_vec = x_n_vec - scalar*inverse_jacobian*f_x_n_vec
		x_1 = new_vec.item(0)
		x_2 = new_vec.item(1)
	return(x_1,x_2)

###########################
#SOLUTION
###########################
#(6.290343468085258e-17, 1.0)
#APPROXIMATELY x_1 = 0,x_2 = 1


#####################################
#COMPUTATIONAL EXERCISE 1
#####################################

def newton_method_fun(x,function,derivative,delta):
	count = 0
	while(abs(function(x)) >= delta):
		x = x - function(x)/derivative(x)
		print("Current Value: ",x,"Current Iteration: ", count)
		count += 1
	return x



def secant_method_fun(x_curr,x_prev,delta,function):
	count = 0
	while(abs(function(x_curr)) >= delta):
		numerator = x_curr - x_prev
		denominator = function(x_curr) - function(x_prev)
		new = x_curr - (numerator/denominator)*function(x_curr)
		x_prev = x_curr
		x_curr = new
		print("Current Value: ",x_curr,"Current Iteration: ", count)
		count += 1
	return x_curr




function_one = lambda x : x*(x**2 - 3) + 1
function_two = lambda x : x**3 - 2*math.sin(x)
derivative_one = lambda x : 3*x**2 - 3
derivative_two = lambda x : 3*x**2 - 2*math.cos(x)
delta = 0.000001
print("FUNCTION ONE NEWTON METHOD")
newton_method_fun(2,function_one,derivative_one,delta)
print("FUNCTION TWO NEWTON METHOD")
newton_method_fun(0.5,function_two,derivative_two,delta)
x_1_function_one = 1.6666666666666667
x_1_function_two = -0.32956626476655604
print('FUNCTION ONE SECANT METHOD')
secant_method_fun(x_1_function_one,2,delta,function_one)
print('FUNCTION TWO SECANT METHOD')
secant_method_fun(x_1_function_two,0.5,delta,function_two)



"""
FUNCTION ONE NEWTON METHOD
Current Value:  1.6666666666666667 Current Iteration:  0
Current Value:  1.5486111111111112 Current Iteration:  1
Current Value:  1.53239016186538 Current Iteration:  2
Current Value:  1.5320889893972243 Current Iteration:  3
FUNCTION TWO NEWTON METHOD
Current Value:  -0.32956626476655604 Current Iteration:  0
Current Value:  0.06076922345421276 Current Iteration:  1
Current Value:  -0.0003014178525422989 Current Iteration:  2
Current Value:  3.651284960146106e-11 Current Iteration:  3
FUNCTION ONE SECANT METHOD
Current Value:  1.578125 Current Iteration:  0
Current Value:  1.5381305481871999 Current Iteration:  1
Current Value:  1.532390697687086 Current Iteration:  2
Current Value:  1.532090947751923 Current Iteration:  3
Current Value:  1.5320888869452851 Current Iteration:  4
FUNCTION TWO SECANT METHOD
Current Value:  0.02139714314642721 Current Iteration:  0
Current Value:  -0.0015522183242252484 Current Iteration:  1
Current Value:  4.395294246179425e-07 Current Iteration:  2
"""
