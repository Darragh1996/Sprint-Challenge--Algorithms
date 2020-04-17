#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(n^3), while(a < n _ n _ n) => while(a < n^3),
the code will scale with respect to n^3.

b) O(n log n), there is a for loop which will run n times
and inside it a while loop which run until j is equal to
or greater than n, since j doubles everytime this makes it log n
n multiplied log n => O(n log n)

c) O(n), the bunnyEars function will run one time for each bunny(n) until
n reaches 0

## Exercise II
egg_func(floor, egg_limit = 0, egg_breaks_at=0):
    test_floor = floor - egg_breaks_at // 2
    drop egg from test_floor:
        if egg breaks:
            egg_breaks_at = test_floor
            if egg_breaks_at == limit + 1:
                return egg_breaks_at
            else:
                egg_func(test_floor, egg_limit, egg_breaks_at)
        else:
            egg_limit = test_floor
            egg_func(floor, egg_limit, egg_breaks_at)

I think the run time complexity would be O(log n) due to the fact the number of floors the need to be checked are halfed with each loop.
