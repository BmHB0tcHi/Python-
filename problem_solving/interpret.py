'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.



'''
def isValid(s):
        
        if len(s) % 2 != 0:
             return False
        if len(s) < 2:
             return False
        
        opening = ["(","[","{"]
        closing = [")","]","}"]
        opening_stack = []
        map_brackets={
             "}":"{",
             "]":"[",
             ")":"("
        }
        # number of brackets has to stay zero, to ensure closing brackert == opening brackets
        number_brackets = 0
        for bracket in s:
            print(bracket)
            if bracket in opening:
                number_brackets-=1
                opening_stack.append(bracket)
            if bracket in closing:
                 number_brackets+=1
                 try:
                    if map_brackets[bracket] != opening_stack.pop():
                      return False
                # if stack is empty
                 except IndexError:
                      return False
        # if number of closing brackets dont match
        if number_brackets != 0:
             return False
        
        return True
                  

print(isValid("(("))
