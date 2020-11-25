"""
  * @author Gatsjy
  * @since 2020-11-25
  * realize dreams myself
  * Blog : https://blog.naver.com/gkswndks123
  * Github : https://github.com/gatsjy
"""

stock_buy = True
count = 0
while stock_buy:
    count = count + 1

    if count == 10:
        #break
        stock_buy = False

    print(count)

kakao_stock = 1000
kiwoom_stock = 500

for i in range(0,2):
    kakao_stock += 500
    kiwoom_stock += 1000

if kakao_stock < kiwoom_stock :
    print("키움이 더 높다")

for i in range(1,10):
    for j in range(1,10):
        print("%s * %s = %s" %(i, j, i*j))



