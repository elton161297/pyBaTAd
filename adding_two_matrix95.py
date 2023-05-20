# Program to add or multiply two matrices
# using list comprehension

X = [[1,2,3],
	[4 ,5,6],
	[7 ,8,9]]

Y = [[9,8,7],
	[6,5,4],
	[3,2,1]]

for x in X:
    for y in Y:
        #1st row iteration
        z1=x[0]*y[0]
        z2=x[0]*y[1]
        z3=x[0]*y[2]
        z4=z1+z2+z3
        #2nd row iteration
        a1=x[1]*y[0]
        a2=x[1]*y[1]
        a3=x[1]*y[2]
        a4=a1+a2+a3
        #3rd row iteration
        c1=x[2]*y[0]
        c2=x[2]*y[1]
        c3=x[2]*y[2]
        c4=c1+c2+c3
        
        
    #"The multiplication of two matrix is "
    print(z4,a4,c4)
    

#print(X[2][2])

