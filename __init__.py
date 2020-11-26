"""
  * @author Gatsjy
  * @since 2020-11-26
  * realize dreams myself
  * Blog : https://blog.naver.com/gkswndks123
  * Github : https://github.com/gatsjy
"""

import sys
from kiwoom.kiwoom import *
from PyQt5.QtWidgets import *

class Main():
    def __init__(self):
        print("Main() start")
        self.app = QApplication(sys.argv) #PyQt5로 실행할 파일명을 자동 설정
        self.kiwoom = Kiwoom() #키움 클래스 객체화
        self.app.exec_() #이벤트 루프 실행
        Kiwoom()

if __name__ == "__main__":
    Main()
