import requests
import time


    # "Cookie": "access_token=skF9EdTmSieGDtaX2S59lA; SESSION=20ed3dc4-767f-434a-805d-60ba4a0e1a27; authcode=2022206666;",
# 请求的URL
url = "https://jw.ruc.edu.cn/resService/jwxtpt/v1/xsd/stuCourseCenterController/saveStuXkByRmdx?resourceCode=XSMH0303&apiCode=jw.xsd.courseCenter.controller.StuCourseCenterController.saveStuXkByRmdx"
#如果仅改变payload（要选的课），cookie和token无法成功的话，试着将你的标头（header）中的url复制到这里
'''
url = "https://jw.ruc.edu.cn/resService/jwxtpt/v1/xsd/stuCourseCenterController/saveStuXkByRmdx?resourceCode=XSMH0303&apiCode=jw.xsd.courseCenter.controller.StuCourseCenterController.saveStuXkByRmdx"
'''
# POST请求的头部
headers = {
    "Cookie": "authcode=2022206666; SESSION=6c8fe4aa-e206-41b8-a578-f58f0874f99a; ",
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
    "Token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2MiOiIyMDIyMjAxNDc2IiwiZXhwIjoxNzM0MTE3NjQ2LCJzaWQiOiI2YzhmZTRhYS1lMjA2LTQxYjgtYTU3OC1mNThmMDg3NGY5NmEifQ.68mytQsZrS2hslf2mf_2qk8cTkPam4MJgX6dCl20xOk",
    #这里改为你的token
}

# POST请求的数
new_data={
  "xkcscode7": "0",
  "kkdwbh": "101700",
  "xkfl": [],
  "tzdlb_name": "正常",
  "xkfs_name": "1",
  "kkdw_name": "信息学院",
  "skls_name": {
    "jczy010id": "21001675",
    "jczy013id": "2024-2025-2",
    "queryFlag": "2",
    "kkgl004id": "00410366143",
    "name": [
      "李彤"
    ]
  },
  "jczy007ids": None,
  "jczy003id": "101700",
  "kcbh": "21001675",
  "ktmc_name": "计算机网络02班",
  "kcxz_name": None,
  "kcmc_name": "计算机网络",
  "kcxz": None,
  "xq_name": "中关村校区中关村校区",
  "id": "00410366143",
  "jczy013id": "2024-2025-2",
  "zxs": "96",
  "zxf": "3",
  "kcdl": "7",
  "kclb": "89",
  "khfs": "1",
  "kkgl00401id": None,
  "szkclb": None,
  "falb": "1",
  "xkfsid": "1",
  "xkgl017id": "c134db340000WH",
  "xkgl019id": "c134db390000WH",
  "isTqxd": "0",
  "xkzy": "",
  "trz": "",
  "tzdlb": "01",
  "jczy010id": "21001675",
  "pyfa01201id": None,
  "skfscode": None,
  "skfs_name": None,
  "sksj": [
    {
      "zc": "1-16",
      "zcmx": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16",
      "kssj": 1800,
      "jssj": 2025,
      "xq": "2",
      "jc": "111213",
      "name": "星期二 11-13节 1-16周"
    },
    {
      "zc": "1-16",
      "zcmx": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16",
      "kssj": 1400,
      "jssj": 1645,
      "xq": "2",
      "jc": "070809",
      "name": "星期二 07-09节 1-16周"
    }
  ],
  "xkcscode1": "1",
  "xkcscode23": "0",
  "sfglymkccode": False,
  "sfglctkccode": False,
  "kclbMapper": "89",
  "xklbbh": "16",
  "bllsZyId": "10232539",
  "isSxrz": "",
  "language": "zh",
  "xxklbcode": "",
  "xjc": "0",
  "xkgl001id": "c1343cb40000WH",
  "zydata": {
    "xkgl019id": "c134db390000WH",
    "xklbbh": "16",
    "kclbMapper": "89",
    "kkgl004id": "00410366143",
    "jczy013id": "2024-2025-2",
    "isSxrz": "",
    "xkgl001id": "c1343cb40000WH"
  }
}
def transform_string(input_string):
    # 替换字符串中的内容
    input_string = input_string.replace("None", "None")
    input_string = input_string.replace("false", "False")
    input_string = input_string.replace("true", "True")
    
    return input_string
def convert_values(data):
    if isinstance(data, dict):  # 如果是字典，递归处理每个键值对
        return {key: convert_values(value) for key, value in data.items()}
    elif isinstance(data, list):  # 如果是列表，递归处理每个元素
        return [convert_values(item) for item in data]
    elif data == "None":  # 如果是字符串 "None"，替换为 None
        return None
    elif data == "false":  # 如果是字符串 "false"，替换为 False
        return False
    elif data == "true":  # 如果是字符串 "true"，替换为 True
        return True
    else:  # 其他情况直接返回
        return data
def main():
    count=0
    while True:
        print(type(new_data))
        
        response = requests.post(url, headers=headers, json=new_data)
        print(response.text)
        time.sleep(3)




if __name__ == "__main__":
    main()
# 发送POST请求



