import requests
import time

# 请求的URL
url = "https://jw.ruc.edu.cn/resService/jwxtpt/v1/xsd/stuCourseCenterController/saveStuXkByRmdx?resourceCode=XSMH0303&apiCode=jw.xsd.courseCenter.controller.StuCourseCenterController.saveStuXkByRmdx"
#如果仅改变payload（要选的课），cookie和token无法成功的话，试着将你的标头（header）中的url复制到这里

# POST请求的头部
headers = {
    "Cookie": "access_token=dIRaXmtcTGW0p_DkfypgRA; SESSION=4ce774e8-eab7-47e4-b60e-c1a8528d7b5f; authcode=2022201476",
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
    "Token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2MiOiIyMDIyMjAxNDc2IiwiZXhwIjoxNzA4NTY0MDY1LCJzaWQiOiI0Y2U3NzRlOC1lYWI3LTQ3ZTQtYjYwZS1jMWE4NTI4ZDdiNWYifQ.ZFX23oDOv4HxA-TIii5Fn2c8dGquSgBMoCAPmzVa11Q",
    #这里改为你的token
}

# POST请求的数
data = {"xkcscode7":"0","kkdwbh":"101700","xkfl":[],"tzdlb_name":"正常","xkfs_name":"4","kkdw_name":"信息学院","skls_name":{"jczy010id":"21001714","jczy013id":"2023-2024-2","queryFlag":"2","kkgl004id":"00410321300","name":["李德英"]},"jczy007ids":None,"jczy003id":"101700","kcbh":"21001714","ktmc_name":"图论01班","kcxz_name":None,"kcmc_name":"图论","kcxz":None,"xq_name":"中关村校区","id":"00410321300","jczy013id":"2023-2024-2","zxs":"32","zxf":"2","kcdl":"1","kclb":"66","khfs":"1","kkgl00401id":None,"szkclb":None,"falb":"1","xkfsid":"22","xkgl017id":"c134b4230000WH","xkgl019id":"c134d7580000WH","isTqxd":"0","xkzy":"","trz":"","tzdlb":"01","jczy010id":"21001714","pyfa01201id":None,"skfscode":None,"skfs_name":None,"sksj":[{"zc":"1-16","zcmx":"1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16","kssj":800,"jssj":930,"xq":"3","jc":"0102","name":"星期三 01-02节 1-16周"}],"xkcscode1":"1","xkcscode23":"0","sfglymkccode":False,"sfglctkccode":False,"kclbMapper":"66","xklbbh":"16","bllsZyId":"10232542","isSxrz":"","language":"zh","xxklbcode":""}
    # 改为你需要抢的课

def main():
    while True:
        response = requests.post(url, headers=headers, json=data)
        print(response.text)
        time.sleep(5)

if __name__ == "__main__":
    main()
# 发送POST请求



