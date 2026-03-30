class Solution:
    def isNumber(self, s: str) -> bool:
        seen_digit = False
        seen_exponent = False
        seen_dot = False
        
        for i, char in enumerate(s):
            if char.isdigit():
                seen_digit = True
                
            elif char in ["+", "-"]:
                # A sign is only valid if it's the very first character, 
                # OR if it comes immediately after an 'e' or 'E'.
                if i > 0 and s[i-1] not in ["e", "E"]:
                    return False
                    
            elif char in ["e", "E"]:
                # An exponent is only valid if we haven't seen one yet, 
                # AND we have already seen at least one digit.
                if seen_exponent or not seen_digit:
                    return False
                seen_exponent = True
                # Reset seen_digit to False because we MUST have a new digit after the 'e'
                seen_digit = False 
                
            elif char == ".":
                # A dot is only valid if we haven't seen a dot yet, 
                # AND we haven't seen an exponent yet (decimals aren't allowed in exponents).
                if seen_dot or seen_exponent:
                    return False
                seen_dot = True
                
            else:
                # If it's a letter (other than e/E) or a random symbol, it's invalid.
                return False
                
        # If we reach the end, it's valid as long as the last thing we were looking for 
        # (a digit) was actually found. This naturally catches "1e", "+.", etc.
        return seen_digit