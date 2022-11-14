
def trimSpace(str):
    ans = ' '
    i = 0
    while i < len(str):
        if str[i] != ' ':
             ans += str[i]
        i+=1
    return ans

#Main
string = input().strip()
ans = trimSpace(string)
print(ans)


