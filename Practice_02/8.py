# Given two matrices of dimension n x n, A and B, find their sum. Use list of list to store values of each matrix.

def sum_matrices(n):
    A = []
    B = []
    C = []
    print("Enter elements of matrix A: ")
    for i in range(n):
        A.append([])
        for j in range(n):
            A[i].append(int(input()))
    print("Enter elements of matrix B: ")
    for i in range(n):
        B.append([])
        for j in range(n):
            B[i].append(int(input()))
    for i in range(n):
        C.append([])
        for j in range(n):
            C[i].append(A[i][j] + B[i][j])
    return C

n = int(input("Enter the value of n: "))
print(sum_matrices(n))