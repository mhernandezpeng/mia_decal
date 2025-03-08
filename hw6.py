#Homework 6
#1. 
import numpy as np

arr = np.array(([[2, 3, 5], [4, 6, 8], [11, 13, 17], [7, 10, 13], ]))

def checkPrime(n):
    if n < 2:
        return False
    for i in range(2, int(np.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True    
    

def containsPrimes(arr):
    prime_rows = np.apply_along_axis(lambda row: any(checkPrime(x) for x in row), axis = 1, arr = arr)
    return arr[prime_rows]

print(containsPrimes(arr))

#2
def checkerboard():
   board = np.zeros((8, 8), dtype = int)
   board[::2, ::2] = 1
   board[1::2, 1::2] = 1
   return board

print(checkerboard())

def reverse_checkerboard(): 
    board = np.ones((8,8), dtype = int)
    board[::2, ::2] = 0
    board[1::2, 1::2] = 0
    return board

print(reverse_checkerboard)

#3
universe = np.array(['galaxy', 'clusters'])
def expansion(arr, int):
    return np.array([(" " * int).join(list(word)) for word in arr])

print(expansion(universe, 3))

#4
np.random.seed(123)
stars = np.random.randint(500, 2000, (5, 5))
def secondDimmest(array):
    return np.sort(array, axis = 0)[1]

print(secondDimmest(stars))





