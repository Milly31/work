matrix=[["x","o","x"],["x","o","x"],["o","x","o"]]
def check_rows(matrix):
	for i in matrix:
		if i==["x","x","x"] or ["o","o","o"]:
			return True
	return False
print check_rows(matrix)
def check_cols(matrix):
	for cols in range(0,3):
		if matrix[0][cols]==matrix[1][cols]==matrix[2][cols]:
			return True
	return False
print check_cols(matrix)
def check_diagonal(matrix):
	for i in range(0,2):
		if matrix[0][i]==matrix[1][i+1]==matrix[2][i+2]:
			return True
		elif matrix[2][1]==matrix[1][1]==matrix[0][0]:
				return True
	return False
print check_diagonal(matrix)