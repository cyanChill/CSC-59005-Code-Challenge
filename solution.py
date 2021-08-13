def find_q(A, q):
     '''
     Locate a position (i,j) where 'q' is at in the nxn matrix A, if 'q'
     is not in the matrix, return -1 

          Parameters:
               A (list[list[num]]): An nxn matrix (list of a list of a 
                                    number type)
               q (num): The value we're searching for; should be the 
                        same number type as the numbers in the matrix

          Returns:
               (i,j) (int,int): Returns the position of 'q' as a tuple 
                                of ints 
               -1 (int): Returned if 'q' is not in the matrix
     '''
     n = len(A) - 1      # Get dimension of matrix in terms of indices
     i = 0; j = n                       # Start at the t.r.c. of matrix
     # If 'q' is out of range of matrix entries
     if q < A[0][0] or q > A[n][n]:     
          return -1
     
     # We work our way towards the b.l.c. from t.r.c. to find entry 'q'
     while j >= 0 and i <= n:
          # Loop only stops if we can't go left/down anymore to find a
          # smaller/bigger entry respectively
          if q == A[i][j]:
               return i,j
          elif q < A[i][j]:
               # We can elimate the current column as by the definition
               # of the structure, all entries in the column will be
               # greater than or equal to A[i][j] and since q < A[i][j], 
               # q is less than all entries in the column 
               j -= 1
          else:
               # This else covers for when q > A[i][j]
               # We can elimate the current row as by definition of the
               # structure, all entries in the row will be less than or
               # equal to A[i][j] and since q > A[i][j], q is greater
               # than all entries in the row 
               i += 1
     
     return -1

# Testing Code:
# A is a 5x5 matrix where the values in each row and column is sorted in
# ascending order
A = [[ 1, 5, 8,19,21], 
     [ 3, 5,10,20,23], 
     [ 4, 6,15,21,36], 
     [10,13,18,30,40], 
     [16,17,19,35,45]]

for q in range(0,47):
     i = find_q(A,q)
     if i == -1:
          print(q, 'is not in matrix A')
     else:
          print(q, ' is at position (', i[0], ',', i[1], ') in matrix A', sep = '')
