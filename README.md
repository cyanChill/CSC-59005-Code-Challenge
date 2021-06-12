# CSC 59005 Code Challenge 2 Solution

### Question 2:
For an integer array A of n+1 numbers that are already sorted in ascending order, one unknown number is repeated and put next to it, e.g., for n=5, A is [1,2,2,3,4,5], 2 is repeated. Write an efficient program of time complexity O(log n) to find out which number is repeated.

## Solution Method:
The only search algorithm that has a running time of O(logn) is binary search. However, from simple observations, we can see that we can only find a duplicate using binary serach if all the elements are consecutive (there's no gap between each entry). If the entries were spaced out, we have to resort to a linear search which will require O(n) time to find the duplicate element as we would have no discernible way of telling where a duplicate could be except by going through each element. With binary search on an array of consecutive elements with 1 duplicate, we have a grasp of where the elements are and we can figure out which subarray the duplicate element will be in.

**The rules we follow for finding the duplicate element:**
1. We first find the middle element in the range of all possible elements by adding the first and last element and dividing it by 2 and take the ceiling of it as the difference could be odd, let's call this element ***midentry***.
2. We then find the middle index of the array by adding the start and end index values and dividing it by 2 and take the floor of it as the difference could be odd, lets call this value ***midind***.
3. Before comparing the entry at ***midind*** with ***midentry***, we check the adjacent entries to the entry at ***midind*** to see if it's equal to either of them and if it is, we return that entry.
4. If the adjacent entries to the entry at ***midind*** are not equal it, we compare the entry at ***midind*** with ***midentry***. Depending on the comparison, one of 2 things can occur:
    
    a. If the entry at ***midind*** is less than ***midind***, we can say that the elements in the range is shifted over to the right by 1 due to there being a duplicate element on the left subarray of ***midind***. We then recursively call our function *findrepeated* with the parameters being the array, the original start index, and ***midind*** - 1 (as this will be our new end index as we figured out that the duplicate element is in the left subarray).

    b. If the element at ***midind*** is equal to ***midind***, we can say that up to this point, there has not be any duplicate elements and that the duplicate element is on the right subarray of ***midind***. We then recursively call our function *findrepeated* with the parameters being the array, ***midind*** + 1 (as this will be our new start index as we figured out that the duplicate element is in the right subarray), and the original end index.


### Sample Input 1:
Given our list A, we want to search for the duplicate element.

![alt text](https://github.com/cyanChill/CSC-59005-Code-Challenge-2/blob/main/images/Sample%20Input%201.PNG "Sample Input 1")

![alt text](https://github.com/cyanChill/CSC-59005-Code-Challenge-2/blob/main/images/Sample%20Output%201.PNG "Sample Output 1")

Visualization of Search: Starting from A[2] since our list is of length 6
```
↓: Points to entry at 'midind'; ▼: Points to 'midentry'; •: Points to entry at 'midind' and 'midentry'
    ↓ ▼
1 2 2 3 4 5
```
> We can see when we check the adjacent entries to '2', we see that there's a 2 adjacent to it so we're done.

### Sample Input 2
Given our list B, we want to search for the duplicate element.

![alt text](https://github.com/cyanChill/CSC-59005-Code-Challenge-2/blob/main/images/Sample%20Input%202.PNG "Sample Input 2")

![alt text](https://github.com/cyanChill/CSC-59005-Code-Challenge-2/blob/main/images/Sample%20Output%202.PNG "Sample Output 2")

Visualization of Search: Starting from B[9] since our list is of length 19
```
↓: Points to entry at 'midind'; ▼: Points to 'midentry'; •: Points to entry at 'midind' and 'midentry'
                     •
4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 19 20 21
                                    •
                        14 15 16 17 18 19 19 20 21
                                          ↓  ▼
                                       19 19 20 21
```

### Sample Input 3
Given our list C, we want to search for the duplicate element.

![alt text](https://github.com/cyanChill/CSC-59005-Code-Challenge-2/blob/main/images/Sample%20Input%203.PNG "Sample Input 3")

![alt text](https://github.com/cyanChill/CSC-59005-Code-Challenge-2/blob/main/images/Sample%20Output%203.PNG "Sample Output 3")

Visualization of Search: Starting from C[12] since our list is of length 26
```
↓: Points to entry at 'midind'; ▼: Points to 'midentry'; •: Points to entry at 'midind' and 'midentry'
                           ↓ ▼
-3 -2 -1 0 1 2 3 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21
             ↓ ▼
-3 -2 -1 0 1 2 3 3 4 5 6 7
                   ↓ ▼
               3 3 4 5 6 7
               •
               3 3
```
