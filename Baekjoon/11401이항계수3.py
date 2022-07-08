from math import factorial
import sys

input = sys.stdin.readline()

n, k = map(int,input().split())

print(factorial(n-k)/factorial(k))