#n children have got m pieces of candy. 
#They want to eat as much candy as they can, 
#but each child must eat exactly the same amount of candy
#as any other child. Determine how many pieces 
#of candy will be eaten by all the children together.
#Individual pieces of candy cannot be split.
from math import floor
def candies(n, m):
    if (n > 10 or n < 1) or (m > 100 or m < 2):
        return 0
    elif n > m:
        return 0
    elif n == m:
        return m
    else:
        CandyKids = floor(m / n);
        return CandyKids * n