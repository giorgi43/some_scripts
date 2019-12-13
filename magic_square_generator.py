#/usr/bin/python3
# 2019/02/25
# This code generates n x n MAGIC SQUARE using basic "diagonal"(Siamese method) method. n is odd

# Main method for generating
def generate(n):
	matrixList = createEmptyMatrix(n)
	# Starting coordinates 
	j = 0 # range is [0,n-1]
	i = int((n-1)/2) # range is [0,n-1]

	jLast = 0
	iLast = int((n-1)/2)

	for number in range(1,n*n + 1):
		if matrixList[j][i] == 0:
			matrixList[j][i] = number
		else:
			i = iLast
			j = jLast
			if j == n - 1:
				j = 0
			else:
				j += 1
			matrixList[j][i] = number
		jLast = j
		iLast = i
		if j == 0:
			j = n - 1
		else:
			j -= 1

		if i == n - 1:
			i = 0
		else:
			i += 1

	return matrixList


# Creates empty 2 demensional list for square. every value is 0
def createEmptyMatrix(n):
	emptyList = []
	for i in range(0,n):
		emptyList.append([])
	for i in emptyList:
		for m in range(0,n):
			i.append(0)
	return emptyList


# For printing generated square on the screen
def visualize(squareList):
	for l in squareList:
		print(l)


if __name__ == '__main__':
	n = int(input("n = "))

	if n % 2 != 0:
		print("Magic constant is", int(n*(n*n + 1)/2))
		visualize(generate(n))
	else:
		print("n must be odd")
