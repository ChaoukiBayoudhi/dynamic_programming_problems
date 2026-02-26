t1=(5,3,4)
l1=[5,6]
print(type(t1))
#naive version (time complexity = O(2^n))
def fibonacci_naive(n:int)->int:
    if n<=1:
        return n
    return fibonacci_naive(n-1)+fibonacci_naive(n-2)

import time
n:int=int(input("Enter a number: "))
start_time=time.process_time_ns()
f1=fibonacci_naive(n)
end_time=time.process_time_ns()
print(f"Fibonacci ({n}) [naive] = {f1}")
print(f"Time taken: {end_time-start_time} nanoseconds")

#memoization version (time complexity = O(n))
def fibonacci_memo(n:int,memo={})->int:
    if n<=1:
        return n
    if n in memo:
        return memo[n]
    memo[n]=fibonacci_memo(n-1)+fibonacci_memo(n-2)
    return memo[n]

import sys
sys.setrecursionlimit(100000)
n:int=int(input("Enter a number: "))
start_time=time.process_time_ns()
f1=fibonacci_memo(n)
end_time=time.process_time_ns()
print(f"Fibonacci ({n}) [memo] = {f1}")
print(f"Time taken: {end_time-start_time} nanoseconds")

def fibonacci_tab(n:int)->int:
    l=[0]*(n+1)
    l[1]=1
    for i in range(2,n+1):
        l[i]=l[i-1]+l[i-2]
    return l[n]

while True :
    n:int=int(input("Enter a number: "))
    if(n>=0):
        break
start_time=time.process_time_ns()
f1=fibonacci_tab(n)
end_time=time.process_time_ns()
print(f"Fibonacci ({n}) [memo] = {f1}")
print(f"Time taken: {end_time-start_time} nanoseconds")

#iterative version with space complexity optimization (O(1))
def Fibonacci_iter(n:int)->int:
    f1,f2=0,1
    for _ in range(2,n+1):
        f1,f2=f2,f1+f2
    return f2

while True :
    n:int=int(input("Enter a number: "))
    if(n>=0):
        break
start_time=time.process_time_ns()
f1=Fibonacci_iter(n)
end_time=time.process_time_ns()
print(f"Fibonacci ({n}) [memo] = {f1}")
print(f"Time taken: {end_time-start_time} nanoseconds")








