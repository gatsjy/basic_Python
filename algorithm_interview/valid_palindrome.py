"""
  * @author Gatsjy
  * @since 2020-11-28
  * realize dreams myself
  * Blog : https://blog.naver.com/gkswndks123
  * Github : https://github.com/gatsjy
"""
# 1. 리스트로 변환
import collections
import re
def isPalindrome(self, s: str) -> bool:
    s = s.lower()

    # 정규식으로 불필요한 문자 필터링
    s = re.sub('[^a-z0-9]','', s)

    return s == s[::-1] # 슬라이싱




