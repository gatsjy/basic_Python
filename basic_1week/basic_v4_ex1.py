"""
  * @author Gatsjy
  * @since 2020-11-26
  * realize dreams myself
  * Blog : https://blog.naver.com/gkswndks123
  * Github : https://github.com/gatsjy
"""

class Condition():
    def sell_filtering(self, a_list):
        for key in a_list.keys():
            if 5000 >= a_list[key] :
                print("종목 %s, 가격 %s" % (key, a_list[key]))

class Kiwoon():
    def __init__(self):
        self.a_list = {'네이버' : 6000, '애플' :15000, '다음':3000, '넷플릭스':5000, '구글':100000, '삼성':3000, 'LG':1000, '키움':500, '호랑':8000, '셀트리온':8500, '코난':6050, '컬링':1000,
                  '하이원' : 3200}

        condition = Condition()
        condition.sell_filtering(self.a_list);

Kiwoon();

class Condition():
    def sell_filtering(self, my_dict):
        for key in my_dict.keys():
            if key == "넷플릭스":
                my_dict[key].update({'보유량': int(my_dict[key]['보유량']/2)})

            if key == "애플":
                my_dict[key].update({'보유량': int(my_dict[key]['보유량']/2)})

            if key == "구글":
                my_dict[key].update({'보유량': int(my_dict[key]['보유량']/2)})

        return my_dict

class Kiwoom():
    def __init__(self):
        self.my_dict = {'네이버':{'현재가':3000, '보유량':100}, '애플':{'현재가':10000, '보유량':200}, '다음':{'현재가':4000, '보유량':50}, '넷플릭스':{'현재가':7000, '보유량':200}, '구글':{'현재가':13000, '보유량':30}}

        condition = Condition()
        result = condition.sell_filtering(self.my_dict)
        print(result)

Kiwoom();
