# CSC 59005 Code Challenge 3 Solution

## Question 3:
Given a 2-D square matrix A[n,n] and it is known that the values along each row and each column are sorted in ascending order. Write an efficient program to search for the location of query value q in A: if q is in A, then return the position (i, j); otherwise returns -1.

## Solution Method:
We start from one corner of the matrix where the properties are easily identifiable and kept tracked of and find 'q' starting from that point. The option we have chosen is the top right corner of the matrix as if we want to find 'q' which is a smaller number than the starting position, 'x', all we have to do is work our way left. If we want to find a 'q' that's big, we have to work our way down. The good thing about starting from the top right corner is that we only need to worry about checking in 2 directions (we don't care about checking the right entries or the entries above as we work our way down and left, elimating those entries from the possibilities of where 'q' can be).

**The rules we follow for traversing towards the entry we're searching for, 'q':**
<ol>
<li> If 'q' is equal to the current entry, we're done. We return the current position.</li>
<li> If 'q' is smaller than the current entry, 'x':
    <ol>
    <li> We move left as all elements in the column of 'x'' is greater than or equal to 'x'', therefore q is smaller than all these elements so we can ignore them. If we can no longer move left, we return -1.</li>
    </ol>
<li> If 'q' is greater than the current entry, 'x':</li>
    <ol>
    <li> We move down as all elements in the row of 'x'' is less than or equal to 'x'', therefore q is bigger than all these elements so we can ignore them.  If we can no longer move down, we return -1.</li>
    </ol> 
</ol>


### Sample Input 1:
Given our matrix A, we want to search for q = 6.

![alt text](https://github.com/cyanChill/CSC-59005-Code-Challenge-3/blob/main/images/Sample%20Input%201.PNG "Sample Input 1")

![alt text](https://github.com/cyanChill/CSC-59005-Code-Challenge-3/blob/main/images/Sample%20Output%201.PNG "Sample Output 1")

Visualization of Search: Starting from A[0][4] since A is a 5x5 matrix:
```
 1    5 —  8 — 19 — 21
      |    
 3    5   10   20   23
      |  
 4    6   15   21   36

10   13   18   30   40

16   17   19   35   45
```
> We can see that we found the value where q is based on the path taken.

### Sample Input 2
Given our matrix A, we want to search for q = 29.

![alt text](https://github.com/cyanChill/CSC-59005-Code-Challenge-3/blob/main/images/Sample%20Input%202.PNG "Sample Input 2")

![alt text](https://github.com/cyanChill/CSC-59005-Code-Challenge-3/blob/main/images/Sample%20Output%202.PNG "Sample Output 2")

Visualization of Search: Starting from A[0][4] since A is a 5x5 matrix:
```
 1    5    8   19   21
                     |
 3    5   10   20   23
                     |
 4    6   15   21 — 36
                |
10   13   18 — 30   40
           |
16   17   19   35   45
```
> Since we see that we can't go down any further from entry 19, we return -1 as we claim that 29 is not in the matrix. We know this is true as from our algorithm, we know that the numbers on the right of the path taken are greater than 29, and the numbers left of the path is less than 29.

### Sample Input 3
Given our matrix A, we want to search for q = 14.

![alt text](https://github.com/cyanChill/CSC-59005-Code-Challenge-3/blob/main/images/Sample%20Input%203.PNG "Sample Input 3")

![alt text](https://github.com/cyanChill/CSC-59005-Code-Challenge-3/blob/main/images/Sample%20Output%203.PNG "Sample Output 3")

Visualization of Search: Starting from A[0][4] since A is a 5x5 matrix:
```
 1    5    8 — 19 — 21
           |     
 3    5   10   20   23
           | 
 4    6 — 15   21   36
      |    
10   13   18   30   40
      | 
16 — 17   19   35   45
```
> Since we see that we can't go left any further from entry 16, we return -1 as we claim that 14 is not in the matrix. We know this is true as from our algorithm, we know that the numbers on the right of the path taken are greater than 14, and the numbers left of the path is less than 14.
