"""
  * @author Gatsjy
  * @since 2020-12-05
  * realize dreams myself
  * Blog : https://blog.naver.com/gkswndks123
  * Github : https://github.com/gatsjy
"""
# 리스트는 어떻게 만들고 사용할까?

#
money = 1000
card = 1
if money >= 2000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")

print(1 in [1,2,3,])

pocket = ['paper','cellphone','money']
if 'money' in pocket:
    print("있음")
else:
    print("없음")

treeHit = 0
while treeHit < 10:
    treeHit = treeHit +1
    print("나무를 %d번 찍었습니다" % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")


test_list = ['one','two','three']
for i in test_list:
    print(i)

a = [(1,2),(3,4),(5,6)]
for(first,last) in a:
    print(first+last)

marks = [90,25,67,45,80]
number = 0
for mark in marks:
    number = number+1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." %number)

a= range(10)
print(a)

for i in range(2,10):
    for j in range(1,10):
        print("%d * %d = %d" %(i,j,i*j))

a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)
print(result)

i=0
while True:
    i += 1
    if i>5: break
    print(i*"*")

A = [70,60,55,75,95,90,80,80,85,100]
total = 0
for student in A:
    total += student
print(total)
average = total / len(A)
print(average)