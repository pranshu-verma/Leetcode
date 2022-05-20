"""
https://leetcode.com/problems/subarray-sum-equals-k/
Given an array of integers nums and an integer k, return the total number of sub arrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2
"""
def subarraySum(nums: list, k: int) -> int:
	dp = {0: 1}  # Initially, prefix sum of the array is 0
	curr_sum = 0
	result = 0

	for num in nums:
		curr_sum += num
		diff = curr_sum - k

		result += dp.get(diff, 0)  # Fetch prefix sum for the diff
		dp[curr_sum] = 1 + dp.get(curr_sum, 0)  # Calculate prefix sum for current sum
		print(dp)

	return result


nums = [1, -1, 1, 1, 1, 1]
k = 3
print(subarraySum(nums, k))
