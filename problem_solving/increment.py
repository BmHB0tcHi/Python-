'''
    For a giver list of integers, consider the list as whole number, and increment 1
    return answer as list
'''
digits_x = [1,1,4,9]

print(digits_x[-2])
def increment_digit(digits):
    nines = 0
    i = 1
    if len(digits) == 1:
        if digits[0] != 9:
            digits[0] = digits[0]+1
            return digits
    
    while i <= len(digits) and digits[-i] == 9 :
        nines+=1
        i+=1

    if nines == len(digits):
        digits[0] = 1
        for j in range(1, len(digits)):
            digits[j] = 0
        digits.append(0)
        return digits
    
    digits[-i] = digits[-i] + 1
    for j in range(-i+1, 0,+1):
        digits[j] = 0
    
    return digits

    


result = increment_digit(digits_x)
print(result)