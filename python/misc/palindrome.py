def palindrome(s):
    return s == s[::-1]


s = "racecar"

result = palindrome(s)

if result:
    print("Yes")
else:
    print("No")