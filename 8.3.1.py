def transpose(mat, tr, N):
	for i in range(N):
		for j in range(N):
			tr[i][j] = mat[j][i]
def isSymmetric(mat, N):
	tr = [ [0 for j in range(len(mat[0])) ] for i in range(len(mat)) ]
	transpose(mat, tr, N)
	for i in range(N):
		for j in range(N):
			if (mat[i][j] != tr[i][j]):
				return False
	return True


