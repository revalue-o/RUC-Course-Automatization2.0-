'''
GPT prompt:

帮我使用pyQt5写一个面向对象的程序，实现以下功能：
初始化一个窗口，窗口标题为“RUC自动化选课工具”。
窗口有三个输入框，分别用于输入 Cookie、Token 和 Payload。
三个输入框都为多行输入框
窗口有一个提交按钮，点击后会不断循环触发一个函数，这个函数内容先不用考虑。
这个函数会返回一个字符串，这个字符串会显示在窗口的一个只读文本框中。
随着函数的不断触发，只读文本框中的内容会不断更新。

帮我修改这个程序
1、将原本的Payload改为三个多行输入框，分别用于输入Payload_1、Payload_2、Payload_3,三者合成一个list输入到函数中
2、增加一个动态显示，在函数返回特定值之前让用户感知到程序在运行，比如在只读文本框中显示“正在运行中...”（后面的三个点不断消失又出现）。

帮我写一个函数，实现以下功能：
接受一个字符串作为参数，若字符串中含有'success'，则返回“选课成功”，否则返回“选课失败”。

https://fly63.com/tool/taag/
██████  ██    ██  ██████     ██   ██ ██   ██     ██   ██ ███████ ██      ██████  ███████ ██████  
██   ██ ██    ██ ██           ██ ██  ██  ██      ██   ██ ██      ██      ██   ██ ██      ██   ██ 
██████  ██    ██ ██            ███   █████       ███████ █████   ██      ██████  █████   ██████  
██   ██ ██    ██ ██           ██ ██  ██  ██      ██   ██ ██      ██      ██      ██      ██   ██ 
██   ██  ██████   ██████     ██   ██ ██   ██     ██   ██ ███████ ███████ ██      ███████ ██   ██ 
                                                                                                 
                                                                                                 
'''
import sys
import time
import random
import re
import requests
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QTextEdit, QLabel
import os
import json
os.chdir(os.path.dirname(__file__))

class WorkerThread(QThread):
    # 定义一个信号，用来将结果传递给主线程更新界面
    update_signal = pyqtSignal(str)

    def __init__(self, payloads):
        super().__init__()
        self.payloads = payloads
        self.succeed_payload = []

    def run(self):
        # 在后台线程中运行长时间操作
        count = 0
        while True:
            
            self.update_signal.emit(f"运行中，已进行轮数{str(count)}")
            result = self.send_xk_request(self.payloads)

            # 发出信号更新界面，覆盖之前的内容
            self.update_signal.emit("正在运行中**")
            time.sleep(0.5)
            self.update_signal.emit("正在运行中****")
            time.sleep(0.5)
            self.update_signal.emit("正在运行中******")
            time.sleep(0.5)


            print(result)
            self.update_signal.emit("【日志】"+result)  # 发出最终结果

            # break  # 退出循环

          
    def transform_string(self,input_string):
        # 替换字符串中的内容
        input_string = input_string.replace("null", "None")
        input_string = input_string.replace("false", "False")
        input_string = input_string.replace("true", "True")
        final_dict=eval(input_string)
        if type(final_dict)!=dict:
            print("转换失败")
            return {}
        return final_dict

    def send_xk_request(self,payloads):
        # 这里是模拟的函数内容，可以根据需要替换成实际的逻辑
        # 请求的URL
        '''
        返回值：暂定返回的就是错误信息或正确信息

        '''
        '''

        payloads = [
            self.url_input.text(),
            self.cookie_input.text(),
            self.token_input.text(),
            self.payload1_input.text(),
            self.payload2_input.text(),
            self.payload3_input.text()
        ]
        示例cookie,token:
        "Cookie": "access_token=skF9EdTmSieGDtaX2S59lA; SESSION=20ed3dc4-767f-434a-805d-60ba4a0e1a27; authcode=2022206666;"
        "Token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2MiOiIyMDIyMjAxNDc2IiwiZXhwIjoxNzI2MzQzNzM1LCJzaWQiOiIyMGVkM2RjNC03NjdmLTQzNGEtODA1ZC02MGJhNGEwZTFhMjcifQ.MBPTiBlLx1uUdt4dpF2Jfsgj_Yr2-KqHtF97JvDS_P8"
        '''
        url = "https://jw.ruc.edu.cn/resService/jwxtpt/v1/xsd/stuCourseCenterController/saveStuXkByRmdx?resourceCode=XSMH0303&apiCode=jw.xsd.courseCenter.controller.StuCourseCenterController.saveStuXkByRmdx"

        if payloads[0] != "" and len(payloads[0])>5:
            print("url is not empty")
            url = payloads[0]
        
        cookies = payloads[1].strip()
        token = payloads[2].strip()
        xk_list=[]
        for i in range(3,len(payloads)):
            if payloads[i] != "" and len(payloads[i])>5:
                xk_list.append(payloads[i])
        
        #如果仅改变payload（要选的课），cookie和token无法成功的话，试着将你的标头（header）中的url复制到这里

        # POST请求的头部
        headers = {
            "Cookie": f"{cookies}",
            #这里改为你的cookie，最后的token=不要复制（保持格式一致就是对的）
            
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Accept-Encoding": "gzip, deflate, br",
            "X-Requested-With": "XMLHttpRequest",
            "Content-Type": "application/json",
            "Origin": "https://jw.ruc.edu.cn",
            "Referer": "https://jw.ruc.edu.cn/Njw2017/student/student-choice-center/student-select-course.html",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "Connection": "close",
            "Token": f"{token}",
            #这里改为你的token
        }
        responses=""
        count=0
        display="未知错误"
        if len(self.succeed_payload)==len(xk_list):
            display="全部选课成功，可以关闭程序了\n"
            return display

        for xk in xk_list:
            count+=1
            if count in self.succeed_payload:
                display=f"payload{str(count)}已经成功选课,继续蹲其课程中\n"
                continue
            responses=requests.post(url,headers=headers,json=self.transform_string(xk)).text
        
            if "eywxt.save.cantXkByCopy.error" in responses:
                display=f"payload{str(count)}的课程已经选上\n"
            elif "eywxt.save.stuLimit.error" in responses:
                display=f"payload{str(count)}的选课人数到达上限（正常蹲课中）\n"
            elif  "success" in responses:
                display=f"payload{str(count)}选课成功\n"
                self.succeed_payload.append(xk)
                break
            elif "The Claim 'sid' value doesn't match the required one" in responses:
                display=f"payload{str(count)}的token或cookie已失效，请重新获取token或cookie\n"

            time.sleep(random.randint(2,6))
        print(responses)
        with open("./log.txt","a") as f:
            f.write(responses)



        return display # 获取最新的回显内容

class RUCAutoSelectionApp(QWidget):
    def __init__(self):
        super().__init__()

        # 初始化界面
        self.setWindowTitle("RUC自动化选课工具")
        self.setGeometry(300, 100, 500, 400)
        
        #加一行字
        self.label = QLabel("下面两个框为运行状态显示框和日志/报错显示框", self)

        # 创建输入框和按钮
        self.url_input = QLineEdit(self)
        self.cookie_input = QLineEdit(self)
        self.token_input = QLineEdit(self)

        self.payload1_input = QLineEdit(self)
        self.payload2_input = QLineEdit(self)
        self.payload3_input = QLineEdit(self)

        self.url_input.setPlaceholderText("输入 URL")
        self.cookie_input.setPlaceholderText("输入 Cookie")
        self.token_input.setPlaceholderText("输入 Token")
        self.payload1_input.setPlaceholderText("输入 Payload_1")
        self.payload2_input.setPlaceholderText("输入 Payload_2")
        self.payload3_input.setPlaceholderText("输入 Payload_3")

        # 设置多行输入框
        self.url_input.setFixedHeight(80)
        self.cookie_input.setFixedHeight(80)
        self.token_input.setFixedHeight(80)
        self.payload1_input.setFixedHeight(80)
        self.payload2_input.setFixedHeight(80)
        self.payload3_input.setFixedHeight(80)

        # 创建提交按钮
        self.submit_button = QPushButton("开始蹲课", self)
        self.submit_button.clicked.connect(self.start_function_trigger)

        # 创建只读文本框
        self.output_text = QTextEdit(self)
        self.output_text.setReadOnly(True)

        self.output_text_2 = QTextEdit(self)
        self.output_text_2.setReadOnly(True)

        # 布局
        input_layout = QVBoxLayout()
        input_layout.addWidget(self.url_input)
        input_layout.addWidget(self.cookie_input)
        input_layout.addWidget(self.token_input)
        input_layout.addWidget(self.payload1_input)
        input_layout.addWidget(self.payload2_input)
        input_layout.addWidget(self.payload3_input)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.submit_button)

        layout = QVBoxLayout()
        layout.addLayout(input_layout)
        layout.addLayout(button_layout)
        
        layout.addWidget(self.label)
        layout.addWidget(self.output_text)
        layout.addWidget(self.output_text_2)

        self.setLayout(layout)

    def start_function_trigger(self):
        # 获取输入的 Payload 内容并组合成一个 list
        payloads = [
            self.url_input.text(),
            self.cookie_input.text(),
            self.token_input.text(),
            self.payload1_input.text(),
            self.payload2_input.text(),
            self.payload3_input.text()
        ]
        
        # 创建并启动后台线程
        self.worker_thread = WorkerThread(payloads)
        self.worker_thread.update_signal.connect(self.update_output)  # 连接信号到更新UI的槽
        self.worker_thread.start()

    def update_output(self, message):
        # 每次更新时覆盖之前的文本内容
        if "日志" in message:
            self.output_text_2.append(message)
        self.output_text.setText(message)
        if "可以关闭程序了" in message:
            self.worker_thread.terminate()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RUCAutoSelectionApp()
    window.show()
    sys.exit(app.exec_())


