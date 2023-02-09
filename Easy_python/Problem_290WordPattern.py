'''
Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false
'''

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word = s.split(" ")
        if len(pattern) != len(word):
            return False

        #create two hashmaps
        charToWord = {}
        wordToChar = {}

        for c,w in zip(pattern,word):
            if c in charToWord and charToWord[c] != w:
                return False
            if w in wordToChar and wordToChar[w] != c:
                return False
            charToWord[c] = w
            wordToChar[w] = c
        return True
        