class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        
        def backtrack(current_string, open_count, close_count):
            # Base Case: When the string has reached the maximum allowed length (2 * n)
            if len(current_string) == 2 * n:
                result.append(current_string)
                return
            
            # Choice 1: We can always add an opening parenthesis if we haven't reached 'n'
            if open_count < n:
                backtrack(current_string + "(", open_count + 1, close_count)
                
            # Choice 2: We can only add a closing parenthesis if it matches an existing open one
            if close_count < open_count:
                backtrack(current_string + ")", open_count, close_count + 1)
                
        # Start the recursion with an empty string and 0 counts
        backtrack("", 0, 0)
        return result
