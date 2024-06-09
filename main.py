import requests
import hashlib
import urllib
import random
import json

version = "2.3.0609-Beta"

appid = 'your_app_id'
secretKey = 'your_secret_key'

to = ["zh", "en", "yue", "wyw", "jp", "kor", "fra", "spa", "th", "ara", "ru", "pt", "de", "it", "el", "nl", "pl", "bul",
    "est", "dan", "fin", "cs", "rom", "slo", "swe", "hu", "cht", "vie"]

def getURL(toLang, q):
    myurl = 'https://fanyi-api.baidu.com/api/trans/vip/translate'
    fromLang = 'auto'
    salt = random.randint(32768, 65536)
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    return myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign
def getResult(s):
    global query
    rand = random.randint(0, 27)
    URL = getURL(to[rand], s)
    req = requests.get(URL)
    res = json.loads(req.text)
    query = res['trans_result'][0]['dst']
    print(" [当前内容]", query)

def main():
    print(f"\n 百度生草机 {version}\n 作者B站主页 https://space.bilibili.com/1674232182")
    query = input("\n 输入待生草的内容\n ")
    print("\n 一切就绪，开始生草！\n")
    for i in range(20):
        getResult(query)
    res = requests.get(getURL('zh', query))
    result = json.loads(res.text)['trans_result'][0]['dst']
    print("\n"+"="*20+"生草结果"+"="*20+"\n "+result+"\n"+"="*48+"\n")
    input(" 按下Enter键退出...\n")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        input("\n"+"="*20+f"\n\n 程序出现错误！\n 报错信息如下\n {e}\n 请联系作者以解决问题！\n\n"+"="*20+"\n\n按下Enter键退出...\n")