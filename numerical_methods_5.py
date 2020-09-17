import math

def lagrange_polynomial():
	initial = -5
	correct_fun = lambda x : 1/(x**2 + 1)
	for i in range(41):
		curr_value = initial + i*(10/41)
		print("i: ",i,"Correct Value: ",correct_fun(curr_value),helper(curr_value))



def helper(x):
	result = 0
	initial = -5
	correct_fun = lambda x : 1/(x**2 + 1)
	for i in range(21):
		x_i = initial + i*(10/21)
		cardinal_poly_num = 1
		cardinal_poly_dem = 1
		for j in range(21):
			x_j = initial + j*(10/21)
			if(j != i):
				cardinal_poly_num = cardinal_poly_num*(x - x_j)
				cardinal_poly_dem = cardinal_poly_dem*(x_i - x_j)
		result = result + correct_fun(x_i)*(cardinal_poly_num/cardinal_poly_dem)
	return result



def lagrange_polynomial_chebyshev():
	initial = -5
	correct_fun = lambda x : 1/(x**2 + 1)
	for i in range(41):
		curr_value = initial + i*(10/41)
		print("i: ",i,"Correct Value: ",correct_fun(curr_value),helper_chebyshev(curr_value))


def helper_chebyshev(x):
	result = 0
	initial = -5
	correct_fun = lambda x : 1/(x**2 + 1)
	for i in range(21):
		x_i = 5*math.cos(i*math.pi/20)
		cardinal_poly_num = 1
		cardinal_poly_dem = 1
		for j in range(21):
			x_j = 5*math.cos(j*math.pi/20)
			if(j != i):
				cardinal_poly_num = cardinal_poly_num*(x - x_j)
				cardinal_poly_dem = cardinal_poly_dem*(x_i - x_j)
		result = result + correct_fun(x_i)*(cardinal_poly_num/cardinal_poly_dem)
	return result


def lagrange_polynomial_chebyshev_two():
	initial = -5
	correct_fun = lambda x : 1/(x**2 + 1)
	for i in range(41):
		curr_value = initial + i*(10/41)
		print("i: ",i,"Correct Value: ",correct_fun(curr_value),helper_chebyshev_two(curr_value))


def helper_chebyshev_two(x):
	result = 0
	initial = -5
	correct_fun = lambda x : 1/(x**2 + 1)
	for i in range(21):
		x_i = 5*math.cos(((2*i + 1)*math.pi)/42)
		cardinal_poly_num = 1
		cardinal_poly_dem = 1
		for j in range(21):
			x_j = 5*math.cos(((2*j + 1)*math.pi)/42)
			if(j != i):
				cardinal_poly_num = cardinal_poly_num*(x - x_j)
				cardinal_poly_dem = cardinal_poly_dem*(x_i - x_j)
		result = result + correct_fun(x_i)*(cardinal_poly_num/cardinal_poly_dem)
	return result




lagrange_polynomial_chebyshev_two()