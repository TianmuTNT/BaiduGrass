from requests import get
from hashlib import md5
from urllib.parse import quote
from random import randint, choice
from json import loads

version = "2.4.1.0610-Beta"

appid = 'your_app_id'
secretKey = 'your_secret_key'

to = ["zh", "en", "yue", "wyw", "jp", "kor", "fra", "spa", "th", "ara", "ru", "pt", "de", "it", "el", "nl", "pl", "bul",
        "est", "dan", "fin", "cs", "rom", "slo", "swe", "hu", "cht", "vie"]

def getURL(toLang, q):
    salt = str(randint(32768, 65536))
    return f"https://fanyi-api.baidu.com/api/trans/vip/translate?appid={appid}&q={quote(q)}&from=auto&to={toLang}" \
            f"&salt={salt}&sign={md5((appid+q+salt+secretKey).encode()).hexdigest()}"
def getResult(s, l, i):
    global query
    query = loads(get(getURL(l, s)).text)["trans_result"][0]["dst"]
    print(f" [第{i}次生草]", query)

def main():
    global query
    query = input("\n 百度生草机 "+version+"\n 作者B站主页 https://space.bilibili.com/1674232182\n\n [输入待生草的内容]\n ")
    num = int(input(" [输入生草次数]\n "))
    print("\n 一切就绪，开始生草！\n")
    for i in range(1, num):
        getResult(query, choice(to), i)
    getResult(query, "zh", num)
    input("\n"+"-"*20+"生草结果"+"-"*20+"\n "+query+"\n"+"-"*48+"\n\n 按下Enter键退出...\n")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
       input("\n"+"-"*20+f"\n\n 程序出现错误！\n 报错信息如下\n {e}\n 请联系作者以解决问题！\n\n"+"-"*20+"\n\n按下Enter键退出...\n")