"""
    Replace Character

Given an input string S and two characters c1 and c2, 
you need to replace every occurrence of character c1 with character c2 in the given string
"""
from sys import stdin    

def replaceCharacter(str, c1,c2):
    ans = ''
    for i in range(len(str)):
        if str[i] == c1:
            ans += c2
        else:
            ans += str[i]
    return ans


## Main
#string = stdin.readline().strip();
string = input().strip()
li = input().split()

c1= li[0]
c2 = li[1]

print(replaceCharacter(string, c1,c2))
