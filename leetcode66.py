class Solution:
    def plusOne(self, digits):
        # Start from the last digit and move backwards
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                # If the digit is less than 9, simply increment it and return
                digits[i] += 1
                return digits
            else:
                # If the digit is 9, set it to 0 and continue to the next digit
                digits[i] = 0

        # If all digits were 9, we need to add an extra 1 at the beginning
        return [1] + digits
