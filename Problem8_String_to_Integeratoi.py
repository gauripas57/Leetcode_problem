class Solution:
    def myAtoi(self, s: str) -> int:
        max_int, min_int, number = (2**31) - 1, -2 ** 31, ""
        string = s.strip()
        if not string: return 0
        
        if string[0] == "-":
            number += "-"
            string = string[1:]
        elif string[0] == "+":
            string = string[1:]
        elif not string[0].isnumeric():
            return 0
        
        for char in string:
            if char.isnumeric():
                number += char
            elif:
                break
        if not number or number == "-":
            return 0
        
        if int(number) > max_int : return max_int
        elif int(number) < min_int : return min_int
        
        return int(number)
    
        