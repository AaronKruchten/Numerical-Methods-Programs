#data i 2-d array, first row is x second row is y

def evaluate(data,x):
	a_lst = divided_differences(data)
	output = 0
	for i in range(len(data[0])):
		product = 1
		for j in range(i):
			product = product*(x - data[0][j])

		output = output + a_lst[i]*product
	return output



def divided_differences(data):
	a_lst = []
	for i in range(len(data[0])):
		numerator = data[1][i]
		for j in range(len(a_lst)):
			product = helper(data,i,j)
			numerator = numerator - a_lst[j]*product
		denominator = helper(data,i,i)
		a_lst = a_lst + [numerator/denominator]
	print(a_lst)
	return a_lst



def helper(data,index,number):
	x_data = data[0]
	product = 1
	if(number > 0):
		for i in range(number):
			product = product*(x_data[index] - x_data[i])
	return product


data = [[1,2,3,-4,5],[2,48,272,1182,2262]]

print(evaluate(data,-1))
##########################
#evaluate(data,-1) = 12
########################