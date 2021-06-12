import math

def findrepeated(A: list, start: int, end: int):
    '''
    Finds the duplicate element in a sorted array recursively where the 
    element in the array are consecutive

        Parameters:
            A (list): A sorted list where the elements are consecutive
            start (int): The starting index
            end (int): The ending index

        Returns:
            None: Returned if the elements in the array aren't consecutive
            A[midind]: Returns the repeated element in the array when
                       found
    '''
    # Algorithm only works with O(logn) time if all the elements are
    # consecutive with only 1 repeat and the array isn't empty, and if the 
    # start index is on the end index, we don't need to check anything
    if len(A) == 0 or A[start] + (end - start) - 1 != A[end] or start > end:
        return None
    
    midentry = math.ceil((A[start] + A[end])/2)
    midind = math.floor((start + end)/2)

    # Guarantees that the A[midind] is not a duplicate
    if A[midind] == A[midind - 1] or A[midind] == A[midind + 1]:
        return A[midind]

    if A[midind] < midentry:
        return findrepeated(A, start, (midind - 1))
    else:
        return findrepeated(A, (midind + 1), end)


# Testing Code:
A = [1,2,2,3,4,5]
B = [4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,19,20,21]
C = [-3,-2,-1,0,1,2,3,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]

repeated = findrepeated(A, 0, (len(A) - 1))
print(repeated, "is the repeated element in array A")

repeated = findrepeated(B, 0, (len(B) - 1))
print(repeated, "is the repeated element in array B")

repeated = findrepeated(C, 0, (len(C) - 1))
print(repeated, "is the repeated element in array C")
