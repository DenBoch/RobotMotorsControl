# Разворот на 180

# Reverse Row at specified index in the matrix
def reverseRow(data, index):

	cols = len(data[index])
	for i in range(cols // 2):
		temp = data[index][i]
		data[index][i] = data[index][cols - i - 1]
		data[index][cols - i - 1] = temp

	return data

# Print Matrix data


def printMatrix(data):

	for i in range(len(data)):
		for j in range(len(data[0])):
			print(data[i][j], end=' ')

		print()

# Rotate Matrix by 180 degrees


def rotateMatrix(data):

	rows = len(data)
	cols = len(data[0])

	if (rows % 2):

		# If N is odd reverse the middle
		# row in the matrix
		data = reverseRow(data, len(data) // 2)

		# Swap the value of matrix [i][j] with
		# [rows - i - 1][cols - j - 1] for half
		# the rows size.
		for i in range(rows // 2):
			for j in range(cols):
				temp = data[i][j]
				data[i][j] = data[rows - i - 1][cols - j - 1]
				data[rows - i - 1][cols - j - 1] = temp

		return data


# Driver Code
data = [[1, 2, 3, 4, 5],
		[6, 7, 8, 9, 10],
		[11, 12, 13, 14, 15],
		[16, 17, 18, 19, 20],
		[21, 22, 23, 24, 25]]

# Rotate Matrix
data = rotateMatrix(data)

# Print Matrix
printMatrix(data)

