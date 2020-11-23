"""
  * @author Gatsjy
  * @since 2020-11-23
  * realize dreams myself
  * Blog : https://blog.naver.com/gkswndks123
  * Github : https://github.com/gatsjy
"""
print("Hello world")

print("Hello world" + " Thank you")

print(900629)

print("%s 입니다." % "홍길동")
print("%s 입니다." % "이순신")
print("이름은 %s 이고 %s에 삽니다." %("홍길동", "서울"))

stock_price = 4500
stock_price_type = type(stock_price)
print(stock_price_type)

stock_percent = 3.8
print(stock_percent)
stock_percent_type = type(stock_percent)
print(stock_percent_type)

#string 변수
stock_name = "홀딩스"
print(stock_name)
stock_name_type = type(stock_name)
print(stock_name_type)

#bool 변수
stock_buy = False
print(stock_buy)
stock_buy_type = type(stock_buy)
print(stock_buy_type)

stock_price = 2000
stock_price2 = 2500
stock_result = stock_price + stock_price2
print(stock_result)

stock_name = "키움증권"
stock_price = 3900
stock_up = 3.8
print("%s %s %s" %(stock_name, stock_price, stock_up))

stock_name = "키움증권"
if stock_name == "키움증권":
    print("통과!")

stock_price = 3000
if stock_price > 3000:
    print("통과!1")
elif stock_price >= 3000:
    print("통과!2")
elif stock_price <= 3000:
    print("통과!3")
else:
    print("조건에 해당하는 게 없음!")

stock_price = 2500
if stock_price > 2000 or stock_price < 2500:
    print("2000~2500 사이")
elif stock_price >= 2500 and stock_price <= 3000:
    print("2500~3000 사이")

for i in range(5, 100):
    print(i)

    if i == 50:
        break

for i in range(0,10):
    for k in range(0,5):
        print("for 문 안에 %s for 문 %s" %(i,k))

