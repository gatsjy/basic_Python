"""
  * @author Gatsjy
  * @since 2020-11-28
  * realize dreams myself
  * Blog : https://blog.naver.com/gkswndks123
  * Github : https://github.com/gatsjy
"""

def isPalindrome(self, s:str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    #팰린드롬 여부 판별
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True

str = input()

cnt = int(str)
while cnt > 0:
    cnt = cnt-1
    a = [];
    str = input()
    for char in range(int(str)):
        a.append(input())

    for s in a:
        if isPalindrome(s) :
            print(a)
            break

    print(0)


