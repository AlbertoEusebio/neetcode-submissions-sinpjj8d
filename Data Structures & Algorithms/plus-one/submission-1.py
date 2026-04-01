class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            
            n = digits[i]
            if n+carry < 10:
                digits[i] += carry
                return digits
            else:
                carry = (digits[i]+carry) // 10
                digits[i] = (digits[i]+carry) % 10
                
        if carry:
            return [carry] + digits