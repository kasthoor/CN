"""
Time Complexity : O(N)
Space Complexity : O(1)

N ->length of input string
"""

from sys import stdin

def isPalindrome(str):
    left = 0
    right = len(str) - 1
    
    while left< right:
        if str[left] != str[right]:
            return False
        
        left +=1
        right -= 1
    return True
    

## Main
print('Enter String :')
string = stdin.readline().strip();

ans = isPalindrome(string)

if ans:
    print('The String '+ string +' is a Palindrome')
else:
   print('The String '+ string +' is not a Palindrome') 

