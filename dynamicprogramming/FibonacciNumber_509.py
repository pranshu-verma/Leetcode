"""
https://leetcode.com/problems/fibonacci-number/
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

Example 1:
Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:
Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

Example 3:
Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
"""
def fib(n: int) -> int:
	# Fibonacci formula -> F(N) = F(N-1) + F(N-2)
	# Base case -> F(1) = 1, F(2) = 1
	dp = {}

	def solve(n: int):
		if n == 1 or n == 2:
			return 1
		if n in dp:  # If we have already computed this result, fetch it from cache
			return dp[n]
		dp[n] = solve(n - 1) + solve(n - 2)  # Compute n-1 and n-2 results.
		return dp[n]

	return solve(n)


n = 50
print(fib(n))
