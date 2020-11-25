# 2.4.1 데이터를 담을 수 있는 자료형 중 하나로 튜플이 있다. 튜플은 데이터를 저장하는 자료형 중에서 데이터를 처리하는 속도가 가장 빠르며, 미리 정해놓은 데이터만 관리할 때 사용한다.
a_list = ("키움", "카카오", "대신")
for val in a_list:
    print(val)

for val in ("키움", "카카오", "대신"):
    print(val)

# 2.4.2 리스트 :
# 리스트는 튜플과 다르게 데이터를 추가하거나 수정 및 삭제할 수 있는 자료형이다

a_list = ["키움", "카카오", "네이버"]
a_list.append("대신증권")
print(a_list[3])
a_list[2] = "한주안"
del a_list[2]

for val in a_list:
    print(val)

for idx, val in enumerate(a_list):
    print("인덱스 : %s, 값 : %s" %(idx,val))

# 2.4.3 딕셔너리 :
a_dict = {"키움증권":1300, "카카오증권":1500, "네이버증권":1000}
print(a_dict.get("키움증권"))
print(a_dict['키움증권'])

for key in a_dict.keys():
    print(a_dict.get(key))

for key, value in a_dict.items(): #key와 value 값 모두 가져옴
    print("키값 : %s , value 값 : %s "%(key,value))

a_dict["다음증권"] = 2500
a_dict.update({"다음증권":2500})

# 여러개의 데이터 한 번에 추가하기
a_dict = {"키움증권":1300, "카카오증권":1500, "네이버증권":1000}
a_dict.update({"다음증권":2000, "애플":152000, "삼성":221500, "LG":25800})
print(a_dict)

# 2.4.4 연습문제
sum = 0
for key,value in a_dict.items():
    sum += value
print(sum)

yes = 111000

cnt = 0
for key,value in a_dict.items():
    if yes > value :
        cnt = yes/ value
        yes = yes%value

print(cnt)




