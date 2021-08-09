# -*- coding: utf-8 -*-
"""
This is a program to compute the numbers within a collatz sequence.
Collatz Sequence: if n is odd n=3x+1 ; if n is even n=n/2

Collatz Conjecture: "Every Collatz sequence eventually attains the value 1".

Some background reading:
    https://www.youtube.com/watch?v=094y1Z2wpJg
    file:///C:/Users/kd0nm/Downloads/collatz.pdf

Although I have had some thoughts on the conjecture,
I will not attempt any sort of proof:
    There is a symantics problem: what does it mean to "attain the value of 1"?:
        Obviously, it cannot mean that it ends at 1, because 1 is within a loop
        The same for 2 and 4, as they are also within a loop
        If "attains" means "stops at", then no numbers would actually attain a value of 1
    I am also interested to know if there are other similar algorithms
        does 5n+1 show similar behaviour? is there a loop containing 1?
        what about 3n-1?
    What about zero? is it odd or even?

Ignoring the existential questions, 
we can write a simple program to explore the similar algorithms.
This is more of a programming exercise to try to practice with:
    generators (for efficiently iterating over large ranges)
    the operators library (why use this library, rather than the +,-,/,* operators?)
    counting (how many iterations before reaching 1)
    wrappers (the counting library uses wrappers)
    plots and graphs (what interesting ways can we show the output?)
    
This problem is also an example of an accumulation of knowledge:
    We are building a set of numbers for which the conjecture is true
    Subsequent tests only need to determine if the output is already within the set
    For large numbers, it is less costly to check if a number is in a set, than to repeat the calculation
    The optimal soluction incorporates set comparison logic

"""
from numpy import isin

set_of_true=[]
test_set=[5,6,7,8,9,31,33,41]

def col(n, x=3, c=1):
    """calculates the next value in the sequence the % operator returns the remainder after division (9%4=1)"""
    if n%2 == 0:
        return n/2
    else:
        return n*x+c
    
def isLoop(n):
    #This logic checks if the algorithm is in a known loop
    if n==1 or n==2 or n==4:
        return True
    else:
        return False
    
def isOne(n):
    if n==1:
        return True
    else:
        return False

def in_true_set(n):
    #uses the numpy isin() function to ascertain if the Collatz sequence has already been solved for input n
    return isin(n, set_of_true)
    
def colSeq(n, x=3, c=1):
    '''generates a list of the numbers in the Collatz sequence starting at n'''
    sequence = []
    while n != 1 and (in_true_set(n) == False):
        sequence.append(int(n))
        set_of_true.append(int(n))
        n = col(n, x, c) #finds the next value of n in the collatz sequence
    sequence.append(int(n))
    return sequence

def my_iterator(start, finish, step =1):
    #a generator function that mimics the builtin generator range()
    #the yield statement is what defines a generator object
    #noteworthy: type(my_iterator)=function ; type(my_iterator(1,2))=generator
    i = start
    while i <= finish:
        yield i
        i = i + step
    pass
    
def colRange(lowerBound,upperBound, step=1, x=3, c=1):
    #uses the built-in generator function to 
    #passes a range of numbers to the Collatz sequence generator
    #measures the generated sequences
    #outputs a dictionary of metrics
    d = {}
    for n in my_iterator(lowerBound,upperBound, step):
        seq=colSeq(n, x, c)
        d[n]=seq
    return d
    
def col_sets_of_set(input_set, x=3, c=1):
    answer = {}
    for n in input_set:
        answer[n] = colSeq(n,x,c)
    return answer


"""
We have functions to:
    calculate the next collatz number
    list the numbers in a sequence
    stop the algorithm when it reaches the 1,2,4 loop
    pass multiple values to the sequence generator

now we need to think about how we will use this information:
    create a directed graph of the output?
    do we want a list of the values known to be true?
    do we want to learn what values are true?
        Should this knowledge be referenced when calculating new collatz sequences?
        Should we compare sets or true together?

lets make functions to...
    Generate a sequence of inputs until stopped by operator
    Create Graph objects to store outputs
    Create visual plots of the data being generated

"""

def update_set_of_true(CollatzSequence, knownSolutions = set_of_true):
    
    return knownSolutions



if __name__ == "__main__":
    pass
    


