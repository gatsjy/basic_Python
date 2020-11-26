"""
  * @author Gatsjy
  * @since 2020-11-25
  * realize dreams myself
  * Blog : https://blog.naver.com/gkswndks123
  * Github : https://github.com/gatsjy
"""
class B_school():
    def __init__(self):
        print("b대학교 초기화")

        self.school_name = "b학교"
class A_school():
    def __init__(self):
        print("초기화, 생성자")
        self.student1_name = None

        b = self.math()
        print("수학과 학생 %s" % b)

        b_school = B_school()
        print(b_school.school_name)

    def math(self):
        self.student1_name = "영수"
        name = self.student1_name

        return name

#A_school()

# 상속의 개념
class Parent():
    def __init__(self):
        print("부모입니다.")

        self.money = 50000000

    def home(self):
        return "부모의 집"

class ChildA(Parent):
    def __init__(self):
        print("자식A")

        print("부모의 돈을 물려받을 수 없습니다.")
        print("%s을 물려받았습니다." % self.home())

class ChildB(Parent):
    def __init__(self):
        super().__init__()
        print("자식B")

        print("부모의 돈 %s" % self.money)
        print("%s을 물려받았습니다." % self.home())

ChildA()
ChildB()

