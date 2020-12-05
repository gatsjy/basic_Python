"""
  * @author Gatsjy
  * @since 2020-12-05
  * realize dreams myself
  * Blog : https://blog.naver.com/gkswndks123
  * Github : https://github.com/gatsjy
"""

# 05.1 파이썬 프로그래밍의 핵심, 클래스
class HouseHan:
    lastname = "한"

    def __init__(self, name):
        self.fullname = self.lastname + name

    def setname(self, name):
        self.fullname = self.lastname+name

    def travel(self, where):
        print("%s, %s여행을 가다." %(self.fullname, where))

    def love(self, other):
        print("%s, %s 사랑에 빠졌네" %(self.fullname, other.fullname))

    def __add__(self,other):
        print("%s, %s 결혼했네" %(self.fullname, other.fullname))

class HouseKim(HouseHan):
    lastname = "김"
    def travel(self, where, day):
        print("%s, %s여행 %d일 가네?" %(self.fullname, where, day))

pey = HouseHan("주안")
pey.travel("제주도")

# 연산자 오버라이딩의 예
pay = HouseKim("승희")
pay.travel("제주도",3)

pey.love(pay)
pey+pay

# 연산저 오버로딩의 예


