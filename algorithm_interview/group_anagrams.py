"""
  * @author Gatsjy
  * @since 2020-11-28
  * realize dreams myself
  * Blog : https://blog.naver.com/gkswndks123
  * Github : https://github.com/gatsjy
"""

from typing import List
import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)

        for word in strs:
            # 정렬하여 딕셔너리에 추가
            anagrams[''.join(sorted(word))].append(word)

        return list(anagrams.values())

res = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
res.groupAnagrams(strs)
