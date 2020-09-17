#Python Homework implementation
x = [2.718281828, -3.141592654, 1.414213562, 0.5772156649, 0.3010299957]
y = [1486.2497, 878366.9879, -22.37492, 4773714.647, 0.000185049]

#Forward order
dot_product = 0
for i in range(len(x)):
	dot_product += x[i]*y[i]
print(dot_product)
#1.0251881368296672e-10


#Reverse order
dot_product_reverse = 0
for i in range(-1,-1*len(x)-1,-1):
	dot_product_reverse += x[i]*y[i]
print(dot_product_reverse)
#-1.5643308870494366e-10

#Part c
new_lst = []
for i in range(len(x)):
	new_lst = new_lst + [x[i]*y[i]]
	sorted_new_lst = sorted(new_lst)
	positives = sorted_new_lst[0:2]
	negatives = sorted_new_lst[2:5]

positives = positives[::-1]
positive_sum = 0
for i in range(len(positives)):
	positive_sum += positives[i]

negative_sum = 0
for i in range(len(negatives)):
	negative_sum += negatives[i]

result = positive_sum + negative_sum
print(result)
#0.0

#Part d
new_lst = []
for i in range(len(x)):
	new_lst = new_lst + [x[i]*y[i]]
	sorted_new_lst = sorted(new_lst)
	positives = sorted_new_lst[0:2]

positive_sum = 0
for i in range(len(positives)):
	positive_sum += positives[i]

negatives = negatives[::-1]
negative_sum = 0
for i in range(len(negatives)):
	negative_sum += negatives[i]

result = positive_sum + negative_sum
print(result)
#0.0



