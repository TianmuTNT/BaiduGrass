from requests import post
from hashlib import md5
from random import randint, choice
from json import loads
from pyperclip import copy

version = "2.8.3.0621-Beta"

appid = "your_app_id"
secretKey = "your_secret_key"

to = ["zh", "en", "yue", "wyw", "jp", "kor", "fra", "spa", "th", "ara", "ru", 
    "pt", "de", "it", "el", "nl", "pl", "bul", "est", "dan", "fin", "cs", 
    "rom", "slo", "swe", "hu", "cht", "vie"]

def getResult(lang, i):
    global query, qlist
    salt = str(randint(32768, 65536))
    url = "https://fanyi-api.baidu.com/api/trans/vip/translate"
    params = {"appid":appid,"q":query.encode(),"from":"auto","to":lang,"salt":salt,
            "sign":md5((appid+query+salt+secretKey).encode()).hexdigest()}
    headers = {'Content-Type':'application/x-www-form-urlencoded'}
    res = loads(post(url, params=params, headers=headers).text)["trans_result"]
    print(f"\n [第{i}次生草]")
    qlist = []
    for j in res:
        q = j["dst"]
        print(f" {q}")
        qlist.append(q)
    query = "\n".join(qlist)

def multiInput(msg):
    print(msg)
    lines = []
    while True:
        text = input(" > ")
        if text == ".":
            break
        lines.append(text)
    return "\n".join(lines)

def main():
    global query
    print("\n 百度生草机 "+version+"\n 作者B站主页 https://space.bilibili.com/1674232182\n\n ")
    query = multiInput(" [输入待生草的内容，键入“.”以完成输入]")
    if query.strip() == "":
        raise Exception("不可以输入为空！")
    num = int(input("\n [输入生草次数]\n "))
    if num < 2 or num > 100:
        raise Exception("不符合生草次数要求！（2~100）")
    print("\n 一切就绪，开始生草！")
    for i in range(1, num):
        getResult(choice(to), i)
    getResult("zh", num)
    print("\n"+"="*20+"生草结果"+"="*20+"\n")
    for i in qlist:
        print(f" {i}")
    input("\n"+"="*48+"\n\n 按下Enter键复制并退出...\n")
    copy(query)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        input("\n"+"="*20+"程序报错"+"="*20+f"\n\n {e}\n\n"+"="*48+"\n\n 按下Enter键退出...\n")