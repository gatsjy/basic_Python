"""
  * @author Gatsjy
  * @since 2020-12-05
  * realize dreams myself
  * Blog : https://blog.naver.com/gkswndks123
  * Github : https://github.com/gatsjy
"""

def say_myself(name, old, man=True):
    print("나의 이름은 %s입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다")
    else:
        print("여자입니다.")


say_myself("한주안", 29);
say_myself("한주안",29,man=False);


