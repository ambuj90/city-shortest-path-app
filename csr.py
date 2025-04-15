import numpy as np
from scipy.sparse import csr_matrix

# Create a dense 2D array
dense = np.array([
    [0, 0, 1],
    [1, 0, 0],
    [0, 2, 0]
])

# Convert to sparse matrix (CSR format)
sparse_matrix = csr_matrix(dense)
print("➡️ Sparse Matrix (CSR format):\n", sparse_matrix)

# Show as a regular dense matrix for clarity
print("\n🧾 Sparse Matrix as Dense Array:\n", sparse_matrix.toarray())

# Create a sparse matrix manually using data, rows, and columns
data = [4, 5, 7]
rows = [0, 1, 2]
cols = [0, 2, 1]

sparse_manual = csr_matrix((data, (rows, cols)), shape=(3, 3))
print("\n🛠️ Manually Created Sparse Matrix:\n", sparse_manual.toarray())

# Multiply the first sparse matrix by a dense vector
vector = np.array([1, 2, 3])
result = sparse_matrix.dot(vector)
print("\n🧮 Matrix-Vector Product Result:\n", result)
