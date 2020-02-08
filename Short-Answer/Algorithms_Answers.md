#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)


b) O(2^n)


c) O(n)

## Exercise II

```python
def check_height(n):
    low = 0
    high = n
    while low <= high:
        middle = low + high // 2
        if egg_breaks(middle):
            if(not egg_breaks(middle - 1)):
                return middle - 1
            high = middle - 1

        elif not egg_breaks(middle):
            
            low = middle + 1
    return -1
```

For this question I felt that a binary sort would be the best option. We fist start at the middle floor. If the egg breaks at t that height, we try the floor directly between the ground and the middle floor and we will consider the middle floor to be our new top floor. If it does not, we try the floor directly between the middle floor and the top floor and we will consider our middle to be the bottom floor. Will repeat this process until we find a floor where the egg breaks and does not on the floor bellow. If no floor is found for what ever reason, the method will return -1


