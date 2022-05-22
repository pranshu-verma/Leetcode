"""
https://leetcode.com/problems/coin-change-2/
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.
You may assume that you have an infinite number of each kind of coin.
The answer is guaranteed to fit into a signed 32-bit integer.

Example 1:
Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

Example 2:
Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.

Example 3:
Input: amount = 10, coins = [10]
Output: 1
"""

# Solution 1
def change(amount: int, coins: list) -> int:
	cache = {}

	def dfs(i, a) -> int:
		if a == amount:  # Compare target value
			return 1
		if a > amount:  # Check if amount is out of range
			return 0
		if i >= len(coins):  # Check if index out of bounds
			return 0
		if (i, a) in cache:  # Check if solution already computed
			return cache[i, a]

		# Take current coin and call dfs again for new amount OR skip current coin and increment index with same value
		cache[(i, a)] = dfs(i, a + coins[i]) + dfs(i + 1, a)
		return cache[(i, a)]

	return dfs(0, 0)

# Solution 2
def change(amount: int, coins: list) -> int:
	dp = [0] * (amount + 1)
	dp[0] = 1

	for i in range(len(coins)):
		for j in range(1, amount + 1):
			if j >= coins[i]:
				dp[j] += dp[j - coins[i]]

	return dp[amount]


amount = 5
coins = [1, 2, 5]
print(change(amount, coins))
