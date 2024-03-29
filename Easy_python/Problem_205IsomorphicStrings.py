'''
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
Example 1:

Input: s = "egg", t = "add"
Output: true

'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Hashmap's will be used as DS
        mapST = {}
        mapTS = {}

        for i in range(len(s)):
            c1 = s[i]
            c2 = t[i]

        #to check if mapping of index already exists in Hashmap
            if ((c1 in mapST and mapST[c1] != c2) or 
                (c2 in mapTS and mapTS[c2] != c1)):
                return False

            mapST[c1] = c2
            mapTS[c2] = c1
        
        return True
