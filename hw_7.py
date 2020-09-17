import math

#Problem one
def Trapezoid_Uniform(f,a,b,n):
	prev = a
	increment = (b-a)/n
	curr = prev + increment
	total = 0
	for i in range(0,n):
		diff = curr - prev
		f_value = f(curr) + f(prev)
		total = total + diff*f_value
		prev = curr
		curr = curr + increment
	return(total/2)

#problem Two
function = lambda x : 2**x
print(Trapezoid_Uniform(function,0,4,1000))
#Result
#3.141572653589612


#Computation Problem Three
def Romberg_help(n,f,a,b):
	initial_value  = (1/2)*(b-a)*(f(a) + f(b))
	n_zero_lst = [initial_value]
	for i in range(1,n+1):
		h = (b-a)/(2**i)
		total = 0
		for k in range(1,2**(i-1) + 1):
			total += f(a + (2*k-1)*h)
		new_value = (1/2)*n_zero_lst[i-1] + h*total
		n_zero_lst = n_zero_lst + [new_value]
	return n_zero_lst


#this is the slow way to do it
def Romberg(n,m,f,a,b,lst):
	if(m == 0):
		return lst[n]
	else:
		return Romberg(n,m-1,f,a,b,lst) + (1/(4**m - 1))*(Romberg(n,m-1,f,a,b,lst) - Romberg(n-1,m-1,f,a,b,lst))


#Romber algorithm
def Romberg_wrapper(n,f,a,b):
	n_zero_lst = Romberg_help(n,f,a,b)
	return Romberg(n,n,f,a,b,n_zero_lst)

function = lambda x : math.sqrt(x)
print(Romberg_wrapper(3,function,0,1))










		