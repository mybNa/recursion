#! /usr/bin/python

### Practice Recursion ###

# 1. Give a number 'n' return a list with 0 - n.
# Option 1:
def print_nums(n, res=[]):
    if n == 0:
        return [0]
    else:
        return [n] + print_nums(n-1, res)
        
# Option 2
def print_numbers(n):
    return [n - x for x in range(0, n+1)]
    
    
# Option 3
def print_numbers2(n, res=[]):
    if n == 0:
        return [n]
    else:
        print_numbers2(n-1, res)
        res.append(n)
    return res
