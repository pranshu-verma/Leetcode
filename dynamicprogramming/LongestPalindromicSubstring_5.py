"""
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
"""


def longestPalindrome(s: str) -> str:
	result = ""

	def search(left, right):
		while left >= 0 and right < len(s) and s[left] == s[right]:
			left -= 1
			right += 1
		return s[left + 1: right]

	for i in range(len(s)):
		result = max(search(i, i), search(i, i + 1), result, key=len)

	return result


s = "babad"
print(longestPalindrome(s))
