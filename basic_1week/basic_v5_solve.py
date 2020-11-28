"""
  * @author Gatsjy
  * @since 2020-11-28
  * realize dreams myself
  * Blog : https://blog.naver.com/gkswndks123
  * Github : https://github.com/gatsjy
"""

import sys
s = sys.stdin.readline().rstrip()

list_a = s.split(' ');
if int(list_a[0]) + int(list_a[2]) == int(list_a[4]) :
    print("YES")
else:
    print("NO")